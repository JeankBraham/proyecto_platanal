import os
import shutil
import random

dataset_path = r"D:\Proyectos\Universidad\proyecto_platanal\unorganized_dataset"
output_path = r"D:\Proyectos\Universidad\proyecto_platanal\final_dataset"

train_split = 0.7
val_split = 0.15
test_split = 0.15

for folder in ["training", "validation", "test"]:
    for class_name in ["healthy", "sigatoka"]:
        os.makedirs(os.path.join(output_path, folder, class_name), exist_ok=True)

def split_data(class_name):
    img_path = os.path.join(dataset_path, class_name)
    images = os.listdir(img_path)
    random.shuffle(images)

    total_images = len(images)
    train_end = int(total_images * train_split)
    val_end = train_end + int(total_images * val_split)

    datasets = {
        "training": images[:train_end],
        "validation": images[train_end:val_end],
        "test": images[val_end:]
    }

    for folder, img_list in datasets.items():
        for img in img_list:
            src = os.path.join(img_path, img)
            dst = os.path.join(output_path, folder, class_name, img)
            shutil.copy(src, dst)

for class_name in ["healthy", "sigatoka"]:
    split_data(class_name)

print("📌 División de dataset completada correctamente.")
