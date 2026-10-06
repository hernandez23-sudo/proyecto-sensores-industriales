# Proyecto de Análisis de Sensores Industriales

## Objetivo
Analizar un dataset de 100,000 mediciones simuladas de sensores industriales para identificar patrones de temperatura y vibración, detectar alertas y generar reportes.

## Descripción de los datos
El archivo `data/sensores_industriales.csv` contiene las siguientes columnas:
- `id_registro`: Identificador de la medición.
- `fecha_hora`: Fecha y hora de la lectura.
- `id_sensor`: Identificador del sensor.
- `planta`: Planta industrial donde está instalado.
- `temperatura_c`: Temperatura en grados Celsius.
- `vibracion_mm_s`: Vibración en milímetros por segundo.

**Nota:** Los datos son simulados con fines educativos.

## Requisitos e Instalación
Este proyecto utiliza la librería `pandas`. Sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/hernandez23-sudo/proyecto-sensores-industriales.git
   cd proyecto-sensores-industriales