import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Carga del modelo
model = tf.keras.models.load_model("agente_clasificador_sigatoka.keras")

def preprocess_image(image):
    image = image.resize((256, 256))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    return image

# Función de predicción
def predict(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)[0][0]
    confidence = float(prediction)
    predicted_class = ""
    if confidence >= 0.5:
        predicted_class = "Sigatoka"
    else:
        predicted_class = "Sana"
        confidence = float(1 - prediction) 
    return predicted_class, confidence

# Interfaz web
st.title("🌿 Agente de detección de Sigatoka en Hojas de Banano 🍌")
option = st.radio("Selecciona una opción:", ("Subir imagen", "Usar cámara"))

image = None
if option == "Subir imagen":
    uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)

elif option == "Usar cámara":
    uploaded_file = st.camera_input("Toma una foto")
    if uploaded_file:
        image = Image.open(uploaded_file)

# Predicción
if image:
    st.image(image, caption="Imagen seleccionada", use_container_width=True)
    predicted_class, confidence = predict(image)
    
    # Mostrar resultado
    st.subheader(f"Predicción: {predicted_class}")
    st.write(f"Confianza: {confidence:.0%}")