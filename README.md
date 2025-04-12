# Proyecto: Bananal. Agente Computacional para Detección de Sigatoka en el banano

Proyecto final para la materia de Conceptos Avanzados de Inteligencia Artificial (AY114) de la Maestría en Inteligencia Artificial y Ciencia de Datos.
[Guía de despliegue del proyecto](#Instrucciones-de-despliegue-del-proyecto)

## 📌 Idea Principal

El objetivo de este proyecto es desarrollar un agente computacional en Python (aunque se evaluará si sigue siendo la mejor opción en el futuro) que permita identificar la Sigatoka en los bananales colombianos (y posiblemente del mundo). Se entrenará el modelo mediante el uso de redes neuronales profundas para el procesamiento de imágenes.

La aplicación inicial será una interfaz gráfica que permita al usuario:

-   Subir una foto de una planta para su análisis.
-   Usar la cámara del dispositivo para realizar detección en tiempo real.

## 🎓 Proyección hacia el Proyecto de Grado de la Maestría

Si el agente funciona correctamente, podría presentarse como proyecto de grado. Si se requiere mayor complejidad, se integrará en un dron autónomo que recorrerá la plantación, generando un mapa de calor o geoespacial para ayudar a los agricultores a tomar decisiones.

**Retos técnicos adicionales:**

-   Implementar vuelo autónomo del dron y la georreferenciación.
-   Mejorar la duración de la batería para cubrir grandes áreas.
-   Diseñar un sistema de retorno automático a la estación de carga.

## 🚀 Ideas Futuras para Expansión

-   **HIVEMIND:** Red de drones autónomos que trabajan en conjunto para monitorear más rápido la plantación.

    ![HIVEMIND Drone System](misc/fotos_repo/hivemind.png)

-   **Extensión a otros cultivos:** Entrenar modelos para detectar enfermedades en plátanos y otras plantaciones.

    ![Enfermedades en cultivos](misc/fotos_repo/enfermedades.jpg)

## 🎯 Posible Comportamiento del Agente

1. El usuario sube una imagen o usa la cámara.
2. El modelo analiza la imagen y detecta la roya.
3. El sistema devuelve:
    - Imagen con las áreas afectadas resaltadas.
    - Un nivel estimado de infección.
    - Recomendaciones preventivas y correctivas según el nivel de infección.

![Ejemplo de detección de infección](misc/fotos_repo/ejemplo.jpg)

_Nota:_ Se debe definir si las recomendaciones se presentan en un documento o directamente en la interfaz.

## 📅 Desarrollo del Proyecto

1. **Definición del problema** 📝
    - Describir el propósito, funcionamiento, limitaciones y mejoras posibles.
2. **Identificación de tecnologías** 🔧
    - Evaluar librerías de visión por computador en Python.
    - Posible migración a otro lenguaje para integración con drones.
3. **Desarrollo del proyecto** 💻
    - Implementación en GitHub para un mejor seguimiento.
4. **Documentación del proyecto** 📄
    - Notion (fase inicial).
    - Overleaf (si se convierte en proyecto de grado).
5. **Pruebas** 🔬
    - Creación de datasets de entrenamiento y prueba.
    - Validación del modelo con imágenes y en tiempo real.
6. **Presentación** 🎤
    - Mejorar la presentación de Notion.
    - Crear diapositivas para mostrar la idea, el código y los resultados.

## Instrucciones de despliegue del proyecto

### Prerrequisito: Tener Python 3.11.6. (no estoy seguro si funciona en versiones más recientes).

Para desplegar el proyecto de manera local se deben realizar los siguientes pasos:

1. Clonar el repositorio en el equipo donde se ejecutará el proyecto.
2. Ubicarse en la carpeta del proyecto.
3. Instalar las librerías requeridas (ya sea de manera local o en un entorno virtual) usando el comando: pip install -r requirements.txt
4. El modelo entrenado no está en el repositorio así que hay que comenzar el proceso de entrenamiento usando el siguiente comando en la terminal: yolo task=detect mode=train model=yolov8s.pt data="[DIRECCIÓN DE LA CARPETA DEL PROYECTO]/proyecto_platanal/data.yaml" epochs=60 imgsz=640 batch=16. Este comando entrenará el modelo usando o CPU de manera predeterminada o GPU (en caso de tener una tarjeta gráfica compatible).
   NOTA: El entrenamiento usando CPU se demora mucho más que con GPU. En caso de querer reducir el tiempo de entrenamiento hay que reducir el número de epochs pero esto puede afectar el rendimiento del agente computacional.
5. Una vez haya sido entrenado el agente, quedará guardado en la carpeta runs/detect/train/weights/best.pt. Para ejecutarlo hay que usar el comando: yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=0. Esto activará la cámara y comenzará a detectar objetos.

---
