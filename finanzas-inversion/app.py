"""
Finanzas personales + inversión en bonos — Módulo 1 (MVP)
Carga manual/foto de gastos, ingreso mensual y dashboard de excedente.
Ver spec completa en el repo para los módulos siguientes (categorización
automática, TIR de bonos vía PyOBD, motor de notificaciones).
"""
from datetime import date, datetime
from pathlib import Path

import streamlit as st

import db
from logic import PCT_DEFAULT, PCT_MAX, PCT_MIN, calcular_cuotas

COMPROBANTES_DIR = Path(__file__).parent / "data" / "comprobantes"
FUENTES = ["Mercado Pago", "Cocos Capital", "Otro"]

st.set_page_config(page_title="Finanzas + Inversión", page_icon="💰", layout="centered")
db.init_db()


def mes_actual() -> str:
    return date.today().strftime("%Y-%m")


def formato_ars(monto: float) -> str:
    return f"${monto:,.0f}".replace(",", ".")


def guardar_comprobante(mes: str, archivo) -> str:
    carpeta = COMPROBANTES_DIR / mes
    carpeta.mkdir(parents=True, exist_ok=True)
    nombre = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{archivo.name}"
    destino = carpeta / nombre
    destino.write_bytes(archivo.getbuffer())
    return str(destino.relative_to(Path(__file__).parent))


st.title("💰 Finanzas + Inversión")

mes = st.sidebar.text_input("Mes (YYYY-MM)", value=mes_actual())
pct_inversion = st.sidebar.slider(
    "% del excedente a invertir",
    min_value=PCT_MIN,
    max_value=PCT_MAX,
    value=int(float(db.get_config("pct_inversion", str(PCT_DEFAULT)))),
    help="Rango ajustable 70-80%, definido según el perfil de inversión (moderado, horizonte 1-3 años).",
)
db.set_config("pct_inversion", str(pct_inversion))

tab_dashboard, tab_ingreso, tab_gastos = st.tabs(["📊 Dashboard", "💵 Ingreso", "🧾 Gastos"])

with tab_ingreso:
    st.subheader(f"Ingreso mensual — {mes}")
    ingreso_actual = db.get_ingreso_mensual(mes) or 0.0
    nuevo_ingreso = st.number_input(
        "Ingreso del mes ($)", min_value=0.0, value=float(ingreso_actual), step=1000.0, format="%.2f"
    )
    if st.button("Guardar ingreso"):
        db.set_ingreso_mensual(mes, nuevo_ingreso)
        st.success(f"Ingreso de {mes} guardado: {formato_ars(nuevo_ingreso)}")
        st.rerun()

with tab_gastos:
    st.subheader(f"Cargar gasto — {mes}")
    # La fuente vive fuera del form: los widgets dentro de un st.form no
    # disparan un rerender hasta el submit, así que el file_uploader
    # condicional de más abajo no aparecería a tiempo si estuviera adentro.
    fuente = st.selectbox("Fuente", FUENTES)
    with st.form("form_gasto", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            fecha_gasto = st.date_input("Fecha", value=date.today())
            monto_gasto = st.number_input("Monto ($)", min_value=0.0, step=100.0, format="%.2f")
        with col2:
            concepto = st.text_input("Concepto")
        comprobante = None
        if fuente == "Cocos Capital":
            comprobante = st.file_uploader(
                "Captura de pantalla (opcional)",
                type=["png", "jpg", "jpeg"],
                help="Se guarda para referencia. La extracción automática del monto llega en el próximo módulo.",
            )
        enviado = st.form_submit_button("Agregar gasto")
        if enviado:
            if monto_gasto <= 0 or not concepto:
                st.error("Completá monto y concepto.")
            else:
                comprobante_path = guardar_comprobante(mes, comprobante) if comprobante else None
                db.add_gasto(mes, fecha_gasto.isoformat(), monto_gasto, concepto, fuente, comprobante_path)
                st.success("Gasto agregado.")
                st.rerun()

    st.divider()
    st.subheader("Gastos cargados")
    gastos = db.get_gastos(mes)
    if not gastos:
        st.info("Todavía no cargaste gastos para este mes.")
    else:
        for g in gastos:
            c1, c2, c3, c4, c5 = st.columns([2, 2, 3, 2, 1])
            c1.write(g["fecha"])
            c2.write(formato_ars(g["monto"]))
            c3.write(g["concepto"])
            c4.write(g["fuente"])
            if c5.button("🗑️", key=f"del_{g['id']}"):
                db.delete_gasto(g["id"])
                st.rerun()

with tab_dashboard:
    st.subheader(f"Resumen — {mes}")
    ingreso = db.get_ingreso_mensual(mes) or 0.0
    total_gastos = db.total_gastos(mes)

    if ingreso == 0.0:
        st.warning("Cargá el ingreso mensual en la pestaña 'Ingreso' para ver el excedente.")
    else:
        resultado = calcular_cuotas(ingreso, total_gastos, pct_inversion)

        c1, c2, c3 = st.columns(3)
        c1.metric("Ingreso", formato_ars(ingreso))
        c2.metric("Gastos", formato_ars(total_gastos))
        c3.metric("Excedente", formato_ars(resultado.excedente))

        if resultado.excedente < 0:
            st.error("Este mes los gastos superan el ingreso. No hay excedente para invertir.")
        else:
            st.markdown(f"**Cuota total a invertir ({pct_inversion}% del excedente):** {formato_ars(resultado.cuota_total)}")
            st.markdown(
                f"**Cuotas semanales restantes:** {resultado.semanas_restantes} "
                f"({formato_ars(resultado.cuota_semanal)} por semana, quedan {resultado.dias_restantes} días del mes)"
            )
            if resultado.recalculado:
                st.caption("Recalculado en base a los días restantes del mes (carga a mitad de mes).")
