import tensorflow as tf
import matplotlib.pyplot as plt

data_dir = r"D:\Proyectos\Universidad\proyecto_platanal\final_dataset"

def load_dataset(subset, batch_size=32):
    dataset = tf.keras.utils.image_dataset_from_directory(f"{data_dir}/{subset}", image_size=(256, 256), batch_size=batch_size)
    class_names = dataset.class_names
    return dataset.prefetch(buffer_size=tf.data.AUTOTUNE), class_names # Prefetch para cargar datos en paralelo

train_dataset, class_names = load_dataset("training")
val_dataset, _ = load_dataset("validation")
test_dataset, _ = load_dataset("test")

print("Clases:", class_names)

# Visualización de imágenes (muestreo)
plt.figure(figsize=(12, 12))
for images, labels in train_dataset.take(1):
    for i in range(16):
        # Filas y columnas de la ventana de muestreo
        ax = plt.subplot(4, 4, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()

# Definición de la red neuronal convolucional (CNN)
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(256, 256, 3)),
    
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Clasificación binaria (sana o sigatoka)
])

# Compilación del modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Early Stopping para evitar sobreentrenamiento
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Entrenamiento del modelo
print("🏋️‍♂️ Inicialización del entrenamiento del agente:")
history = model.fit(train_dataset, epochs=30, validation_data=val_dataset, callbacks=[early_stopping])

# Evaluación del modelo en el dataset de prueba
print("📊 Inicialización de la prueba del agente:")
test_loss, test_acc = model.evaluate(test_dataset)
print(f"\n🔹 Precisión en el set de prueba: {test_acc * 100:.2f}%")

# Guardado del modelo
model.save("agente_clasificador_sigatoka.keras")
print("\n✅ Agente guardado correctamente")
