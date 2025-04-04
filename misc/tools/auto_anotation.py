import cv2
import os
import json

def detect_leaf_bbox(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    
    # Crear una máscara para ignorar el padding gris (127, 127, 127)
    mask = cv2.inRange(image, (127, 127, 127), (127, 127, 127))
    
    # Invertir la máscara para detectar la hoja
    mask_inv = cv2.bitwise_not(mask)
    
    # Aplicar la máscara y encontrar contornos
    contours, _ = cv2.findContours(mask_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Encontrar el contorno más grande (asumiendo que es la hoja)
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        return x, y, w, h
    
    return None

def modify_bbox(image, bbox):
    x, y, w, h = bbox
    while True:
        temp_image = image.copy()
        cv2.rectangle(temp_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Ajustar Bounding Box", temp_image)
        key = cv2.waitKey(0) & 0xFF
        
        if key == ord('w'):
            y -= 5  # Mover arriba
        elif key == ord('s'):
            y += 5  # Mover abajo
        elif key == ord('a'):
            x -= 5  # Mover izquierda
        elif key == ord('d'):
            x += 5  # Mover derecha
        elif key == ord('q'):
            w -= 5  # Reducir ancho
        elif key == ord('e'):
            w += 5  # Aumentar ancho
        elif key == ord('z'):
            h -= 5  # Reducir altura
        elif key == ord('c'):
            h += 5  # Aumentar altura
        elif key == ord('r'):
            return None  # Rechazar bounding box
        elif key == 13:  # Enter para confirmar
            cv2.destroyAllWindows()
            return x, y, w, h

def visualize_bbox(image_path, bbox):
    image = cv2.imread(image_path)
    if bbox:
        x, y, w, h = bbox
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Bounding Box", image)
        key = cv2.waitKey(0) & 0xFF
        cv2.destroyAllWindows()
        
        if key == ord('y'):  # Aceptar
            return bbox
        elif key == ord('n'):  # Modificar
            return modify_bbox(image, bbox)
    return None

def generate_annotations(root_folder):
    category_mapping = {
        "black_sigatoka": "sigatoka",
        "healthy_leaves": "healthy"
    }
    
    for subset in ["training", "validation"]:
        subset_folder = os.path.join(root_folder, subset)
        output_json = os.path.join(root_folder, f"{subset}_annotations.json")
        annotations = []
        image_id = 1
        
        if not os.path.exists(subset_folder):
            continue
        
        for category in os.listdir(subset_folder):
            category_folder = os.path.join(subset_folder, category)
            if not os.path.isdir(category_folder):
                continue
            
            category_name = category_mapping.get(category, "unknown")
            
            for filename in os.listdir(category_folder):
                if filename.endswith(('.jpg', '.png', '.jpeg')):
                    image_path = os.path.join(category_folder, filename)
                    bbox = detect_leaf_bbox(image_path)
                    
                    if bbox:
                        bbox = visualize_bbox(image_path, bbox)
                        if bbox:
                            x, y, w, h = bbox
                            annotation = {
                                "image_id": image_id,
                                "file_name": filename,
                                "bbox": [x, y, w, h],
                                "category": category_name  # Guardar categoría como texto
                            }
                            annotations.append(annotation)
                            image_id += 1
        
        if annotations:
            with open(output_json, "w") as json_file:
                json.dump({"annotations": annotations}, json_file, indent=4)
            print(f"Anotaciones guardadas en {output_json}")

if __name__ == "__main__":
    root_folder = r"D:\Proyectos\Universidad\proyecto_platanal\final_dataset"  # Carpeta raíz con training, validation y test
    generate_annotations(root_folder)
