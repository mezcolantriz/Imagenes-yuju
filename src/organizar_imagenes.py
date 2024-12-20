import os
import shutil

# Ruta base de la carpeta train
train_dir = r'C:\Users\solan\OneDrive\Desktop\4GEEKS\Imagenes-yuju\data\train'
cat_dir = os.path.join(train_dir, 'cat')  # Subcarpeta para gatos
dog_dir = os.path.join(train_dir, 'dog')  # Subcarpeta para perros

# Crear carpetas para cat y dog si no existen
os.makedirs(cat_dir, exist_ok=True)
os.makedirs(dog_dir, exist_ok=True)

# Mover archivos etiquetados a sus respectivas carpetas
for filename in os.listdir(train_dir):
    file_path = os.path.join(train_dir, filename)  # Ruta completa del archivo
    if os.path.isfile(file_path):  # Asegurarse de que es un archivo
        if filename.startswith('cat'):
            shutil.move(file_path, os.path.join(cat_dir, filename))
        elif filename.startswith('dog'):
            shutil.move(file_path, os.path.join(dog_dir, filename))

print("¡Imágenes organizadas en carpetas 'cat' y 'dog' correctamente!")

