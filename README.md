# Proyecto de Curvas IDF – Región de Atacama, Chile

**Carpeta base:** C:/Seba/P1_E2_14052025/Actualv2/Resultados/hidrologia

Este directorio contiene la estructura modular y reproducible para el análisis y generación de curvas IDF (Intensidad-Duración-Frecuencia) de precipitaciones, siguiendo buenas prácticas de ciencia de datos y normativa internacional.

## Estructura de carpetas

- 00_Exploracion_Inicial
- 01_Ingesta_Limpieza
- 02_Analisis_Exploratorio
- 03_Homogeneidad_PeriodoComun
- 04_Outliers
- 05_Desagregacion
- 05-1_Analisis_Frecuencia_24h
- 05-3_Analisis_Frecuencia_Completo
- 06_Graficos_IDF_Finales
- 07_Reporte_Final
- 07_Verificaciones_Finales

Cada carpeta contiene scripts, logs, resultados y gráficos exclusivos de su etapa. El flujo es completamente trazable y auditable.

---

## Reglas de gestión
- Solo se consideran las 7 estaciones especificadas.
- Todos los scripts y logs se guardan en la carpeta correspondiente.
- Los resultados intermedios y finales se exportan en formatos reproducibles (CSV, Excel, PDF, PNG).
- Los logs documentan cada filtro, limpieza, ajuste y decisión tomada.

---

## Ejecución recomendada
- Ejecuta el pipeline desde el script principal (`main.py`) para mantener la reproducibilidad y trazabilidad.
- Cada módulo puede ejecutarse de forma independiente para depuración o auditoría.

---

## Contacto
Responsable: [Tu Nombre o Equipo]
