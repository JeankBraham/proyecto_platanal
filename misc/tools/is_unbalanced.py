import os

data_dir = r"D:\Proyectos\Universidad\proyecto_platanal\final_dataset"
subsets = ["training", "validation", "test"]

for subset in subsets:
    print(f"\n📂 {subset.upper()} SET:")
    for class_name in os.listdir(os.path.join(data_dir, subset)):
        class_path = os.path.join(data_dir, subset, class_name)
        if os.path.isdir(class_path):
            num_images = len(os.listdir(class_path))
            print(f"  {class_name}: {num_images} imágenes")
