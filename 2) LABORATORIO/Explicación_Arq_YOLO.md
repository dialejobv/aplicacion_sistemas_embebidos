# YOLO (You Only Look Once)
<p align="justify">
YOLO, que significa "You Only Look Once" (Solo miras una vez), es una familia de arquitecturas de redes neuronales para detección de objetos en tiempo real, este trata la detección como un único problema de regresión, en palabras sencillas da solo una mirada la imagen y permite la predicción simultánea de los cuadros delimitadores y las clases de los objetos, lo que permite que sea bastante ágil, capaz de procesar decenas o cientos de fotogramas por segundo, esto permite que sea usado en diferentes aplicaciones desde la conducción autónoma, transporte inteligente en ciudades inteligentes, robótica, salud y educación [1].
</p>

## ¿Cómo funciona YOLO?

Su funcionamiento de manera resumida se puede exponer en los siguientes pasos:
1. **División de la imagen:** Toma la imagen de entrada y la divide en una cuadrícula (por ejemplo, 13x13 o 19x19 celdas).
2. **Predicción por celda:** Cada celda de la cuadrícula es responsable de predecir un cierto número de cuadros delimitadores. Para cada cuadro, predice:
* Las coordenadas (centro, ancho, alto).
* Una "puntuación de confianza" (qué tan seguro está de que hay un objeto ahí).
* Las probabilidades de clase (qué objeto es).
3. **Post-procesamiento:** Finalmente, se utiliza una técnica llamada Supresión No Máxima (NMS) para eliminar las predicciones duplicadas y quedarse con la más precisa para cada objeto [2].

## Breve Historia de YOLO

Los hitos más relevantes en la historia de YOLO fue:
<p align="justify">
2015: El Nacimiento (YOLOv1): El Nacimiento (YOLOv1) - Joseph Redmon y Ali Farhadi presentan la idea revolucionaria de un detector de "un solo disparo", cambiando el paradigma de los detectores de "dos etapas" como R-CNN.
</p>
<p align="justify">
2016-2018: La Consolidación (YOLOv2, YOLOv3): Redmon mejora la precisión y la capacidad de detectar objetos pequeños con mejoras en la arquitectura (como Darknet-53) y la predicción multiescala.
</p>
<p align="justify">
2020: El Salto a la Industria (YOLOv5): Glenn Jocher y Ultralytics lanzan YOLOv5, implementado en PyTorch. Esto lo hace mucho más fácil de usar, accesible y se convierte en un estándar de la industria.
</p>
<p align="justify">
2023-2024: La Era de la Eficiencia y la Versatilidad (YOLOv8, YOLOv9, YOLOv10):  Ultralytics lanza YOLOv8, un marco de trabajo unificado para detección, segmentación y estimación de pose. Aparecen YOLOv9 (centrado en la eficiencia computacional con PGI y GELAN) y YOLOv10 (que elimina la necesidad de NMS).
</p>
<p align="justify">
2025-2026: El Estado del Arte (YOLO11 y YOLO26): Se lanza YOLO11, que ofrece mejor precisión con menos parámetros. Finalmente, en 2026, llega YOLO26, el último modelo de Ultralytics, que incorpora un diseño "end-to-end" que elimina por completo el paso de post-procesamiento (NMS) y es hasta un 43% más rápido en CPUs [3],[4],[5].
</p>

# Tabla de Comparación Principales Versiones de YOLO
<p align="justify">
A continuación se expondrá una tabla que muestra las versiones más importantes de YOLO, con sus respectivas características y rendimientos, teniendo presente la variable denominada **mAP** que significa **mean Average Precisión**, es fundamental tener presente que cada YOLO tiene diferentes variantes del modelo (como es el caso del nano, small, medium, large y x-large).
</p>
<img width="1766" height="692" alt="image" src="https://github.com/user-attachments/assets/0611a98b-15ff-49d0-b8fc-2d4bff5eb246" />

<p align="justify">
Nota: Aunque actualmente se expone un YOLOv12 y un YOLOv13 que son versiones que la comunidad está desarrollando, las fuentes oficiales como Ultralitycs no recomiendan su uso en producción porque aún presentan problemas de inestabilidad, mayor consumo de memoria y ganancia de precisión marginales.
</p>

# Comparación de YOLO con otros modelos de Visión Artificial

A continuación se presentan otros modelos de visión computacional, que es importante tener presente:

<img width="1752" height="858" alt="image" src="https://github.com/user-attachments/assets/dc47835f-7878-4e28-b058-f1529f0b0287" />

# Ejemplo de uso YOLO
<p align="justify">
A continuación se expone un ejemplo sencillo con YOLOv8 para que los estudiantes lo utilicen, con su respectivo paso a paso en el pc de manera remota:
</p>

1. **Creación de entorno virtual:** Es importante que el estudiante cree su entorno virtual, para ello se le recomienda instalar **virtualenv** como se ha hecho en clase o también que se use la creación del entorno virtual por medio de anaconda o miniconda. Posteriormente el estudiante debe ir a la carpeta Scripts si trabaja con Windows o en la de include si es con linux y escribir .\Activate, para activar el entorno virtual.

2. **Instalación de Librerías:** Como se está trabajando con python el estudiante debe generar la siguiente instalación de las librerías:

```python
pip install ultralytics opencv-python matplotlib
```

3. Posteriormente el estudiante debe escribir el siguiente código y correrlo con **python nombre_archivo.py**:

```python
import cv2
from ultralytics import YOLO

# Cargar modelo
model = YOLO('yolov8n.pt')

# Abrir cámara
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error al abrir la cámara")
    exit()

print("Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar inferencia en el frame actual
    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow('Detección en tiempo real', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

Teniendo el siguiente resultado:

<img width="1456" height="1064" alt="image" src="https://github.com/user-attachments/assets/ee7f69a7-48bf-429b-a995-6aa35e9ff01c" />

La arquitectura de YOLOv8 es (para más información consultar[7]: 

<img width="1542" height="1580" alt="image" src="https://github.com/user-attachments/assets/d76a47b5-e0f8-4add-b081-992e38105230" />


## Referencias: 


[1] “YOLO: un detector de objetos en tiempo real”, Innovatiana.com. [En línea]. Disponible en: https://www.innovatiana.com/es/post/what-is-yolo-in-ai. [Consultado: 01-abr-2026].

[2] A. Vina, “Descubrir la evolución de la detección de objetos: De YOLO a YOLO11”, Ultralytics.com. [En línea]. Disponible en: https://www.ultralytics.com/es/blog/the-evolution-of-object-detection-and-ultralytics-yolo-models. [Consultado: 01-abr-2026].

[3] SO Development, “Comparación de YOLOv12 y YOLOv13: La evolución de la detección de objetos en tiempo real”, SO Development, 07-jul-2025. [En línea]. Disponible en: https://es.so-development.org/comparing-yolov12-and-yolov13-the-evolution-of-real-time-object-detection/. [Consultado: 01-abr-2026].

[4] Ultralytics, “YOLOv5 vs. YOLOv8: Evaluando la Evolución de la IA de Visión de Ultralytics”, Ultralytics.com, 01-abr-2025. [En línea]. Disponible en: https://docs.ultralytics.com/es/compare/yolov5-vs-yolov8/. [Consultado: 01-abr-2026].

[5] Ultralytics.com. [En línea]. Disponible en: https://docs.ultralytics.com/es/compare/ . [Consultado: 01-abr-2026].

[6] Opensistemas.com. [En línea]. Disponible en: https://opensistemas.com/yolo11-mas-rapido-mas-preciso-mas-versatil/. [Consultado: 01-abr-2026].

[7] J. Solawetz, “What is YOLOv8? A Complete Guide”, Roboflow Blog, 23-oct-2024. [En línea]. Disponible en: https://blog.roboflow.com/what-is-yolov8/. [Consultado: 02-abr-2026].

