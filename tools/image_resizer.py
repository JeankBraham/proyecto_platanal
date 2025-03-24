from PIL import Image, ImageOps
import os

input_folder = r"C:\Users\USUARIO\Desktop\dataset\training\real\black_sigatoka"
output_folder = r"C:\Users\USUARIO\Desktop\resized_dataset\training\real\black_sigatoka"
target_size = (256, 256)  

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        img = Image.open(os.path.join(input_folder, filename))
        img = ImageOps.pad(img, target_size, color=(127, 127, 127))
        img.save(os.path.join(output_folder, filename))

print("Padding aplicado correctamente.")
