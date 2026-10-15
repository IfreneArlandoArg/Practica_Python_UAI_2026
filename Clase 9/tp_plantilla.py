"""Plantilla del TP Integrador NumPy: red de monitoreo de calidad del aire.

Completá cada función `parte_X` siguiendo la consigna del TP. No modifiques
`generar_datos()` salvo la constante LEGAJO.
"""

from __future__ import annotations

import numpy as np

LEGAJO = 12345  # Reemplazar por tu número de legajo
UMBRAL = 35.0  # µg/m³
DIAS = 14
HORAS = 24


def titulo(texto: str) -> None:
    """Imprime un título subrayado."""
    print(f"\n{texto}")
    print("-" * len(texto))


def generar_datos(legajo: int) -> tuple[np.ndarray, np.ndarray]:
    """Genera los barrios y la matriz de mediciones (6, DIAS * HORAS).

    Cada sensor tiene un nivel base propio, un ciclo diario (picos a las 8 y
    19 h) y ruido aleatorio. Un 2 % de las mediciones falla y se marca con -1.

    Args:
        legajo: Semilla del generador aleatorio.

    Returns:
        Tupla (barrios, mediciones).
    """
    rng = np.random.default_rng(legajo)
    barrios = np.array(["Centro", "Puerto", "Norte", "Sur", "Parque", "Industrial"])
    base = np.array([30.0, 38.0, 22.0, 26.0, 12.0, 48.0]).reshape(-1, 1)

    horas = np.arange(DIAS * HORAS) % HORAS
    ciclo = 8 * np.exp(-((horas - 8) ** 2) / 8) + 10 * np.exp(-((horas - 19) ** 2) / 8)
    ruido = rng.normal(0, 4, size=(len(barrios), DIAS * HORAS))

    mediciones = np.clip(base + ciclo + ruido, 1, None)
    fallas = rng.random(mediciones.shape) < 0.02
    mediciones[fallas] = -1
    return barrios, mediciones


def parte_1(mediciones: np.ndarray) -> None:
    """Exploración y vectorización (puntos 1 a 3)."""
    titulo("Parte 1 - Exploración y vectorización")
    validas = mediciones[mediciones != -1]
    print(f"Forma de la matriz: {mediciones.shape}")
    print(f"Tipo de dato: {mediciones.dtype}")
    print(f"Cantidad de mediciones válidas: {validas.size}")
    print(f"Cantidad de fallas: {np.count_nonzero(mediciones == -1)}")
    print(f"Valor mínimo: {validas.min():.2f} µg/m³")
    print(f"Valor promedio: {validas.mean():.2f} µg/m³")
    print(f"Valor máximo: {validas.max():.2f} µg/m³")


def parte_2(mediciones: np.ndarray) -> np.ndarray:
    """Limpieza de datos (puntos 4 a 7). Devuelve los datos con NaN."""
    titulo("Parte 2 - Limpieza de datos")
    datos = mediciones.astype(float).copy()
    datos[datos == -1] = np.nan
    print(f"Se reemplazaron {np.count_nonzero(np.isnan(datos))} valores inválidos por NaN.")
    return datos


def parte_3(datos: np.ndarray) -> np.ndarray:
    """Reshape, indexación y slicing (puntos 8 a 10). Devuelve datos 3D."""
    titulo("Parte 3 - Reorganización y slicing")
    datos3d = datos.reshape(-1, DIAS, HORAS)
    print(f"Forma final 3D: {datos3d.shape}")
    print(f"Primer barrio, primer día, primeras 6 horas: {datos3d[0, 0, :6]}")
    return datos3d


def parte_3b(datos3d: np.ndarray, barrios: np.ndarray) -> None:
    """Unión, división y ordenamiento (puntos 11 y 12)."""
    titulo("Parte 3b - Unión, división y ranking")
    promedio_por_barrio = np.nanmean(datos3d, axis=(1, 2))
    ranking = np.argsort(promedio_por_barrio)[::-1]
    print("Ranking de barrios por promedio general:")
    for posicion, indice in enumerate(ranking, start=1):
        print(f"  {posicion}. {barrios[indice]}: {promedio_por_barrio[indice]:.2f} µg/m³")


def parte_4(datos3d: np.ndarray, barrios: np.ndarray) -> np.ndarray:
    """Estadística por ejes (puntos 13 a 16). Devuelve promedios diarios (6, 14)."""
    titulo("Parte 4 - Estadística por ejes")
    promedios_diarios = np.nanmean(datos3d, axis=2)
    print(f"Forma de promedios diarios: {promedios_diarios.shape}")
    print(f"Promedio diario del barrio Centro: {promedios_diarios[0]}")
    return promedios_diarios


def parte_5(datos: np.ndarray) -> None:
    """Simulación con números aleatorios (puntos 17 y 18)."""
    titulo("Parte 5 - Números aleatorios")
    rng = np.random.default_rng(LEGAJO)
    simulacion = rng.normal(loc=np.nanmean(datos), scale=np.nanstd(datos), size=(6, 14))
    print(f"Promedio simulado: {simulacion.mean():.2f} µg/m³")
    print(f"Desvío simulado: {simulacion.std():.2f} µg/m³")
    print(f"Fracción por encima del umbral {UMBRAL} µg/m³: {(simulacion > UMBRAL).mean() * 100:.2f}%")


def clasificar_aire(promedios_diarios: np.ndarray) -> np.ndarray:
    """Clasifica cada promedio diario como Bueno, Moderado, Malo o Crítico.

    Umbrales: < 12, < 35, < 55 y >= 55 µg/m³. Debe estar vectorizada.
    """
    condiciones = [
        promedios_diarios < 12,
        (promedios_diarios >= 12) & (promedios_diarios < 35),
        (promedios_diarios >= 35) & (promedios_diarios < 55),
        promedios_diarios >= 55,
    ]
    etiquetas = ["Bueno", "Moderado", "Malo", "Crítico"]
    return np.select(condiciones, etiquetas, default="Crítico")


def parte_6(promedios_diarios: np.ndarray, barrios: np.ndarray) -> None:
    """Reporte final (puntos 20 y 21)."""
    titulo("Parte 6 - Reporte final")
    clases = clasificar_aire(promedios_diarios)
    promedio_general = np.nanmean(promedios_diarios)
    barrio_peor = barrios[np.nanargmax(np.nanmean(promedios_diarios, axis=1))]
    print(f"Promedio general de la red: {promedio_general:.2f} µg/m³")
    print(f"Barrio con mayor promedio: {barrio_peor}")

    print("\nResumen por barrio:")
    categorias = ["Bueno", "Moderado", "Malo", "Crítico"]
    for i, barrio in enumerate(barrios):
        promedio_barrio = np.nanmean(promedios_diarios[i])
        maximo_diario = np.nanmax(promedios_diarios[i])
        dias_criticos = np.count_nonzero(clases[i] == "Crítico")
        conteo = {categoria: np.count_nonzero(clases[i] == categoria) for categoria in categorias}
        print(f"  {barrio:>10}: promedio {promedio_barrio:.2f}, máximo {maximo_diario:.2f}, días críticos {dias_criticos}")
        print(f"    Distribución: {conteo}")


def main() -> None:
    barrios, mediciones = generar_datos(LEGAJO)
    parte_1(mediciones)
    datos = parte_2(mediciones)
    datos3d = parte_3(datos)
    parte_3b(datos3d, barrios)
    promedios_diarios = parte_4(datos3d, barrios)
    parte_5(datos)
    parte_6(promedios_diarios, barrios)


if __name__ == "__main__":
    main()
