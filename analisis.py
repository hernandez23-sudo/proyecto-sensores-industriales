import pandas as pd
import os

# Cargar datos usando rutas relativas
ruta_csv = os.path.join('data', 'sensores_industriales.csv')
df = pd.read_csv(ruta_csv)

# Asegurar que fecha_hora sea datetime
df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])

print("Analisis de datos de sensores industriales")

# R1: Cantidad de registros y sensores distintos
total_registros = len(df)
total_sensores = df['id_sensor'].nunique()
print(f"\n1. Total de registros: {total_registros}")
print(f"   Total de sensores distintos: {total_sensores}")

# R2: Temperatura promedio de cada planta
print("\n2. Temperatura promedio por planta:")
promedios = df.groupby('planta')['temperatura_c'].mean()
print(promedios)

# R3: Temperatura máxima, sensor y fecha (manejo de empates)
max_temp = df['temperatura_c'].max()
df_max = df[df['temperatura_c'] == max_temp]
print(f"\n3. Temperatura máxima registrada: {max_temp} °C")
print("   Registros con la temperatura máxima (empates):")
for index, row in df_max.iterrows():
    print(f"   - Sensor: {row['id_sensor']} | Fecha: {row['fecha_hora']} | Planta: {row['planta']}")

# R4: Contar lecturas con temperatura > 85 °C
umbral = 85
df_alertas = df[df['temperatura_c'] > umbral]
cantidad_alertas = len(df_alertas)
print(f"\n4. Cantidad de lecturas con temperatura > {umbral} °C: {cantidad_alertas}")

# R5: Planta con más alertas (manejo de empates)
if cantidad_alertas > 0:
    alertas_por_planta = df_alertas.groupby('planta').size()
    max_alertas = alertas_por_planta.max()
    plantas_top = alertas_por_planta[alertas_por_planta == max_alertas]
    print(f"\n5. Planta(s) con más alertas ({max_alertas} alertas):")
    for planta, count in plantas_top.items():
        print(f"   - {planta}")
else:
    print("\n5. No se encontraron alertas de temperatura.")

# R6: Exportar alertas a resultados/alertas.csv
if not os.path.exists('resultados'):
    os.makedirs('resultados')

ruta_salida = os.path.join('resultados', 'alertas.csv')
df_alertas.to_csv(ruta_salida, index=False)
print(f"6. Archivo exportado exitosamente en: {ruta_salida}")