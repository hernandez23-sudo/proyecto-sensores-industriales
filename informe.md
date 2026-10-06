# Informe de Aplicación de Big Data

## 5. Las 5 V aplicadas al proyecto

| V | Explicación | Ejemplo concreto | ¿Está en el CSV actual o es futuro? |
| :--- | :--- | :--- | :--- |
| **Volumen** | Cantidad de datos generados. | 100,000 registros en el CSV. | Actual (100k). Futuro: miles de sensores enviando cada segundo (Terabytes). |
| **Velocidad** | Rapidez de generación y procesamiento. | Lecturas cada minuto en el CSV. | Actual. Futuro: lecturas cada segundo. |
| **Variedad** | Diferentes tipos de datos. | Datos tabulares (CSV). | Actual Futuro: fotografías y reportes de texto. |
| **Veracidad** | Calidad y confiabilidad de los datos. | Sensores pueden fallar o dar lecturas erróneas. | Futuro al ampliar el sistema, la calidad se vuelve crítica. |
| **Valor** | Utilidad del dato para tomar decisiones. | Detectar alertas > 85°C para prevenir fallos. | Actual. Futuro: mantenimiento predictivo. |

## 6. Tipos de datos y procesamiento tradicional

**Clasificación:**
- **El CSV de sensores:** Estructurado filas y columnas definidas.
- **Un mensaje JSON enviado por un sensor:** Semiestructurado tiene etiquetas pero no un esquema rígido tabular.
- **Una fotografía de una máquina:** No estructurado datos binarios/imágenes.
- **El texto libre de un reporte de mantenimiento:** No estructurado lenguaje natural.

**¿Por qué 100,000 registros no son Big Data automáticamente?**
100,000 registros caben perfectamente en la memoria RAM de una computadora estándar y pueden procesarse con Excel o Pandas en segundos. No cumplen con la "V" de Volumen de Big Data. Las limitaciones al aumentar la escala serían: falta de memoria RAM, tiempos de procesamiento insostenibles y la incapacidad de procesar datos en tiempo real.

## 7. Batch y Streaming

- **Tipo de procesamiento realizado:** **Batch (por lotes)**. Justificación: Se analiza un archivo CSV estático que ya está guardado. No hay procesamiento en tiempo real.
- **Alerta en pocos segundos (>85°C):** Se usaría **Streaming**. El sensor enviaría el dato y un sistema como Apache Kafka o Spark Streaming lo procesaría inmediatamente al recibirlo.
- **Resumen al final del día:** Se usaría **Batch**. Se acumulan todos los datos del día y se procesan en un bloque al finalizar la jornada.

## 8. Lambda y Kappa

**Escenario A (Combinar histórico por lotes + recientes rápido):**
Arquitectura **Lambda**.
*Diagrama:* 
`Fuente -> [Capa Batch (Histórico)] -> Vista Batch`
`Fuente -> [Capa Speed (Tiempo real)] -> Vista Speed`
`Vista Batch + Vista Speed -> Capa Serving -> Consulta`

**Escenario B (Una sola lógica, reprocesar eventos):**
Arquitectura **Kappa**.
*Diagrama:*
`Fuente -> [Cola de mensajes (Kafka)] -> [Motor de Stream (Spark/Flink)] -> Almacenamiento`
*(Si hay error, se reinicia el stream desde el principio de la cola).*

## 9. Analítica descriptiva, predictiva y prescriptiva

- **Descriptiva:** 
  1. La temperatura promedio de la planta X es de Y °C (basado en tu ejecución de `analisis.py`).
  2. Se detectaron Z lecturas con temperatura mayor a 85 °C.
- **Predictiva:** 
  Pregunta: ¿Es probable que el sensor S-123 falle en los próximos 7 días?
  Datos adicionales: Historial de mantenimiento previo del sensor, edad del sensor, y correlación entre vibración alta y fallos previos.
- **Prescriptiva:** 
  Acción: Ante un riesgo previsto de fallo en el sensor S-123, la empresa debería programar una parada de mantenimiento preventivo en la próxima hora de baja producción.
  Información a revisar: Costo de la parada vs. Costo de la reparación de emergencia, y disponibilidad de repuestos.