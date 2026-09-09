"""Cálculo de excedente y cuotas de inversión (Módulo 2 de la spec)."""
import calendar
import math
from dataclasses import dataclass
from datetime import date

PCT_DEFAULT = 75
PCT_MIN = 70
PCT_MAX = 80


@dataclass
class ResultadoCuotas:
    excedente: float
    cuota_total: float
    dias_restantes: int
    semanas_restantes: int
    cuota_semanal: float
    recalculado: bool  # True si hoy no es el día 1 del mes (carga a mitad de mes)


def calcular_excedente(ingreso: float, total_gastos: float) -> float:
    return ingreso - total_gastos


def calcular_cuotas(
    ingreso: float,
    total_gastos: float,
    pct_inversion: float,
    hoy: date | None = None,
) -> ResultadoCuotas:
    hoy = hoy or date.today()
    excedente = calcular_excedente(ingreso, total_gastos)
    cuota_total = max(0.0, excedente) * (pct_inversion / 100)

    ultimo_dia = calendar.monthrange(hoy.year, hoy.month)[1]
    fin_de_mes = date(hoy.year, hoy.month, ultimo_dia)
    dias_restantes = (fin_de_mes - hoy).days + 1
    semanas_restantes = max(1, math.ceil(dias_restantes / 7))
    cuota_semanal = cuota_total / semanas_restantes

    return ResultadoCuotas(
        excedente=excedente,
        cuota_total=cuota_total,
        dias_restantes=dias_restantes,
        semanas_restantes=semanas_restantes,
        cuota_semanal=cuota_semanal,
        recalculado=hoy.day != 1,
    )
