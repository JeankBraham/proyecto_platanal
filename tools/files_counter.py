import os

def count_images(route, extensions=("jpg", "jpeg")):
    total = 0
    for root, _, files in os.walk(route):
        total += sum(1 for file in files if file.lower().endswith(extensions))
    return total

dataset_dir = r"D:\Proyectos\Universidad\proyecto_platanal\unorganized_dataset"
total = count_images(dataset_dir)
print(f"Total de imágenes en '{dataset_dir}': {total}")
print("Imágenes para entrenamiento (70%): " + str(int(total*0.7)))
print("Imágenes para prueba (15%): " + str(int(total*0.15)))
print("Imágenes para validación (15%): " + str(int(total*0.15)))