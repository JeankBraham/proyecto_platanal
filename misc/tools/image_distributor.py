import os
import shutil
import random

healthy_path = r"D:\Proyectos\Universidad\proyecto_platanal\unorganized_dataset\healthy"
sigatoka_path = r"D:\Proyectos\Universidad\proyecto_platanal\unorganized_dataset\sigatoka"
output_path = r"D:\Proyectos\Universidad\proyecto_platanal\final_dataset"

healthy_samples = 250
sigatoka_samples = 250
train_split = 0.8

for folder in ["training", "validation"]:
    os.makedirs(os.path.join(output_path, folder), exist_ok=True)

def split_data():
    healthy_images = [img for img in os.listdir(healthy_path)]
    sigatoka_images = [img for img in os.listdir(sigatoka_path)]

    selected_healthy = random.sample(healthy_images, healthy_samples)
    selected_sigatoka = random.sample(sigatoka_images, sigatoka_samples)

    all_images = [(os.path.join(healthy_path, img), img) for img in selected_healthy] + \
                 [(os.path.join(sigatoka_path, img), img) for img in selected_sigatoka]

    random.shuffle(all_images)

    train_end = int(len(all_images) * train_split)
    datasets = {
        "training": all_images[:train_end],
        "validation": all_images[train_end:]
    }

    for folder, img_list in datasets.items():
        for src_path, img_name in img_list:
            dst_path = os.path.join(output_path, folder, img_name)
            shutil.copy(src_path, dst_path)

split_data()

print("✅ Muestreo y división completados correctamente.")
