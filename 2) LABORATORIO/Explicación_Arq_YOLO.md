# YOLO (You Only Look Once)
<p align="justify">
YOLO, que significa "You Only Look Once" (Solo miras una vez), es una familia de arquitecturas de redes neuronales para detección de objetos en tiempo real, este trata laa detección como un único problema de regresión, en palabras sencillas da solo una miradaa la imagen y permite la predicción simultánea de los cuadros delimitadores y las clases de los objetos, lo que permite que sea bastante ágil, capaz de procesar decenas o cientos de fotogramas por segundo, esto permite que sea usado en diferentes aplicaciones desde la conducción autónoma, transporte inteligente en ciudades inteligentes, robótica, salud y edu ación [[1](https://www.innovatiana.com/es/post/what-is-yolo-in-ai)].
</p>

## ¿Cómo funciona YOLO?

Su funcionamiento de manera resumida se puede exponer en los siguientes pasos:
1. **División de la imagen:** Toma la imagen de entrada y la divide en una cuadrícula (por ejemplo, 13x13 o 19x19 celdas).
2. **Predicción por celda:** Cada celda de la cuadrícula es responsable de predecir un cierto número de cuadros delimitadores. Para cada cuadro, predice:
* Las coordenadas (centro, ancho, alto).
* Una "puntuación de confianza" (qué tan seguro está de que hay un objeto ahí).
* Las probabilidades de clase (qué objeto es).
3. **Post-procesamiento:** Finalmente, se utiliza una técnica llamada Supresión No Máxima (NMS) para eliminar las predicciones duplicadas y quedarse con la más precisa para cada objeto. [[2](https://www.ultralytics.com/es/blog/the-evolution-of-object-detection-and-ultralytics-yolo-models)]

## Breve Historia de YOLO

Los hitos más relevantes en la historia de YOLO fue:

**2015: El Nacimiento (YOLOv1):** El Nacimiento (YOLOv1) - Joseph Redmon y Ali Farhadi presentan la idea revolucionaria de un detector de "un solo disparo", cambiando el paradigma de los detectores de "dos etapas" como R-CNN.

**2016-2018: La Consolidación (YOLOv2, YOLOv3):** Redmon mejora la precisión y la capacidad de detectar objetos pequeños con mejoras en la arquitectura (como Darknet-53) y la predicción multiescala.

**2020: El Salto a la Industria (YOLOv5):** Glenn Jocher y Ultralytics lanzan YOLOv5, implementado en PyTorch. Esto lo hace mucho más fácil de usar, accesible y se convierte en un estándar de la industria.

**2023-2024: La Era de la Eficiencia y la Versatilidad (YOLOv8, YOLOv9, YOLOv10):**  Ultralytics lanza YOLOv8, un marco de trabajo unificado para detección, segmentación y estimación de pose. Aparecen YOLOv9 (centrado en la eficiencia computacional con PGI y GELAN) y YOLOv10 (que elimina la necesidad de NMS).

**2025-2026: El Estado del Arte (YOLO11 y YOLO26):** Se lanza YOLO11, que ofrece mejor precisión con menos parámetros. Finalmente, en 2026, llega YOLO26, el último modelo de Ultralytics, que incorpora un diseño "end-to-end" que elimina por completo el paso de post-procesamiento (NMS) y es hasta un 43% más rápido en CPUs [[3]( https://es.so-development.org/comparing-yolov12-and-yolov13-the-evolution-of-real-time-object-detection/)],[[4](https://docs.ultralytics.com/es/compare/yolov5-vs-yolov8/)],[[5](https://opensistemas.com/yolo11-mas-rapido-mas-preciso-mas-versatil/)].

# Tabla de Comparación Principales Versiones de YOLO



## Referencias: 


[1] “YOLO: un detector de objetos en tiempo real”, Innovatiana.com. [En línea]. Disponible en: https://www.innovatiana.com/es/post/what-is-yolo-in-ai. [Consultado: 01-abr-2026].

[2] A. Vina, “Descubrir la evolución de la detección de objetos: De YOLO a YOLO11”, Ultralytics.com. [En línea]. Disponible en: https://www.ultralytics.com/es/blog/the-evolution-of-object-detection-and-ultralytics-yolo-models. [Consultado: 01-abr-2026].

[3] SO Development, “Comparación de YOLOv12 y YOLOv13: La evolución de la detección de objetos en tiempo real”, SO Development, 07-jul-2025. [En línea]. Disponible en: https://es.so-development.org/comparing-yolov12-and-yolov13-the-evolution-of-real-time-object-detection/. [Consultado: 01-abr-2026].

[4] Ultralytics, “YOLOv5 vs. YOLOv8: Evaluando la Evolución de la IA de Visión de Ultralytics”, Ultralytics.com, 01-abr-2025. [En línea]. Disponible en: https://docs.ultralytics.com/es/compare/yolov5-vs-yolov8/. [Consultado: 01-abr-2026].

[5] Ultralytics.com. [En línea]. Disponible en: https://docs.ultralytics.com/es/compare/)][[6](https://opensistemas.com/yolo11-mas-rapido-mas-preciso-mas-versatil/. [Consultado: 01-abr-2026].

[6] Opensistemas.com. [En línea]. Disponible en: https://opensistemas.com/yolo11-mas-rapido-mas-preciso-mas-versatil/. [Consultado: 01-abr-2026].

