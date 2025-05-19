"""
Script: exploracion_inicial.py
Propósito: Diagnóstico y filtrado inicial de estaciones para el flujo IDF Atacama.
Ubicación: 00_Exploracion_Inicial
Autor: Cascade AI
Fecha: 2025-05-18
"""
import pandas as pd
from pathlib import Path
import shutil
import os

# --- Configuración ---
BASE_DIR = Path(r"C:/Seba/P1_E2_14052025/Actualv2/Resultados/hidrologia/00_Exploracion_Inicial")
EXCEL_ORIGEN = BASE_DIR / "estaciones.xlsx"  # Debes poner aquí tu archivo fuente
EXCEL_RESPALDO = BASE_DIR / "estaciones_respaldo.xlsx"
EXCEL_FILTRADO = BASE_DIR / "estaciones_filtradas.xlsx"
LOG = BASE_DIR / "log.txt"

ESTACIONES_OBJETIVO = [
    "JORQUERA EN LA GUARDIA",
    "MANFLAS HACIENDA",
    "LAUTARO EMBALSE",
    "LOS LOROS",
    "ELIBOR CAMPAMENTO",
    "PASTOS GRANDES",
    "COPIAPO"
]

# --- 1. Respaldo del archivo fuente ---
if EXCEL_ORIGEN.exists():
    shutil.copy(EXCEL_ORIGEN, EXCEL_RESPALDO)
else:
    raise FileNotFoundError(f"No se encontró el archivo de estaciones: {EXCEL_ORIGEN}")

# --- 2. Leer y filtrar solo las estaciones objetivo ---
df = pd.read_excel(EXCEL_ORIGEN)

# Normalizar nombres para filtrar (insensible a mayúsculas/minúsculas)
def normaliza(s):
    return str(s).strip().upper()
df['NOM_ESTACION_NORM'] = df['Nombre_Estacion'].apply(normaliza)
estaciones_norm = [e.upper() for e in ESTACIONES_OBJETIVO]

filtro = df['NOM_ESTACION_NORM'].isin(estaciones_norm)
df_filtrado = df[filtro].copy()

# --- 3. Diagnóstico de años, faltantes y duplicados ---
reporte = []
for est in estaciones_norm:
    sub = df_filtrado[df_filtrado['NOM_ESTACION_NORM'] == est]
    if sub.empty:
        reporte.append(f"❌ Estación NO encontrada: {est}")
        continue
    años = sub['Año'].drop_duplicates().sort_values()
    n_anios = len(años)
    faltantes = sub['Precip_max'].isna().sum()
    duplicados = sub.duplicated(subset=['Año']).sum()
    reporte.append(f"{est}: {n_anios} años, {faltantes} faltantes, {duplicados} duplicados")

# --- 4. Exportar filtrado y log ---
df_filtrado.to_excel(EXCEL_FILTRADO, index=False)

with open(LOG, "a", encoding="utf-8") as f:
    f.write("\n--- Exploración inicial ---\n")
    for linea in reporte:
        f.write(linea + "\n")
    f.write(f"\nFiltrado exportado: {EXCEL_FILTRADO}\n")

print(f"✔ Exploración inicial completada. Ver {EXCEL_FILTRADO} y log.txt")
