from PIL import Image, ImageOps
import os

input_folder = r"D:\Proyectos\Universidad\proyecto_platanal\dataset\training\healthy_leaves"
output_folder = r"C:\Users\USUARIO\Desktop\resized\healthy"
target_size = (256, 256)  

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith((".jpg", ".jpeg")):
        img = Image.open(os.path.join(input_folder, filename))
        img = ImageOps.pad(img, target_size, color=(127, 127, 127))
        img.save(os.path.join(output_folder, filename))

print("Padding aplicado correctamente.")
