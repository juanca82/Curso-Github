import cv2
import imghdr

def detectar_matriculas(imagen):
    # Cargar la imagen
    img = cv2.imread(imagen)

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Cargar el clasificador Haar Cascade pre-entrenado para la detección de matrículas
    cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

    # Detectar las matrículas en la imagen
    matriculas = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))

    # Dibujar rectángulos alrededor de las matrículas detectadas
    for (x, y, w, h) in matriculas:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar la imagen con las matrículas detectadas
    cv2.imshow('Matriculas Detectadas', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ruta de la imagen de entrada
imagen = '/Users/juancamiloocampozapata/Desktop/Matricula.jpg'

# Comprobar si el archivo es una imagen
if imghdr.what(imagen):
    detectar_matriculas(imagen)
else:
    print('El archivo no es una imagen.')
