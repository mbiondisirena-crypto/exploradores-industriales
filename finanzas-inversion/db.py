"""Capa de datos: SQLite local para ingresos, gastos y configuración."""
import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "finanzas.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS ingresos (
    mes TEXT PRIMARY KEY,           -- 'YYYY-MM'
    monto REAL NOT NULL,
    actualizado_en TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mes TEXT NOT NULL,              -- 'YYYY-MM'
    fecha TEXT NOT NULL,            -- 'YYYY-MM-DD'
    monto REAL NOT NULL,
    concepto TEXT NOT NULL,
    fuente TEXT NOT NULL,           -- 'Mercado Pago' | 'Cocos Capital' | 'Otro'
    comprobante_path TEXT,
    creado_en TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS config (
    clave TEXT PRIMARY KEY,
    valor TEXT NOT NULL
);
"""


@contextmanager
def get_conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    with get_conn() as conn:
        conn.executescript(SCHEMA)


def _now():
    return datetime.now(timezone.utc).isoformat()


def set_ingreso_mensual(mes: str, monto: float):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO ingresos (mes, monto, actualizado_en) VALUES (?, ?, ?) "
            "ON CONFLICT(mes) DO UPDATE SET monto=excluded.monto, actualizado_en=excluded.actualizado_en",
            (mes, monto, _now()),
        )


def get_ingreso_mensual(mes: str) -> float | None:
    with get_conn() as conn:
        row = conn.execute("SELECT monto FROM ingresos WHERE mes=?", (mes,)).fetchone()
        return row["monto"] if row else None


def add_gasto(mes: str, fecha: str, monto: float, concepto: str, fuente: str, comprobante_path: str | None = None):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO gastos (mes, fecha, monto, concepto, fuente, comprobante_path, creado_en) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (mes, fecha, monto, concepto, fuente, comprobante_path, _now()),
        )


def get_gastos(mes: str) -> list[sqlite3.Row]:
    with get_conn() as conn:
        return conn.execute(
            "SELECT * FROM gastos WHERE mes=? ORDER BY fecha DESC, id DESC", (mes,)
        ).fetchall()


def delete_gasto(gasto_id: int):
    with get_conn() as conn:
        conn.execute("DELETE FROM gastos WHERE id=?", (gasto_id,))


def total_gastos(mes: str) -> float:
    with get_conn() as conn:
        row = conn.execute("SELECT COALESCE(SUM(monto), 0) AS total FROM gastos WHERE mes=?", (mes,)).fetchone()
        return row["total"]


def get_config(clave: str, default: str | None = None) -> str | None:
    with get_conn() as conn:
        row = conn.execute("SELECT valor FROM config WHERE clave=?", (clave,)).fetchone()
        return row["valor"] if row else default


def set_config(clave: str, valor: str):
    with get_conn() as conn:
        conn.execute(
            "INSERT INTO config (clave, valor) VALUES (?, ?) "
            "ON CONFLICT(clave) DO UPDATE SET valor=excluded.valor",
            (clave, valor),
        )
