import cv2

# Ruta de la imagen
ruta_imagen = '/Users/juancamiloocampozapata/Desktop/Matricula.jpg'

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)

# Verificar si la imagen se ha cargado correctamente
if imagen is None:
    print("No se pudo cargar la imagen:", ruta_imagen)