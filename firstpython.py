# Display thw Output
print ("New Python file")

from PIL import Image

try:
    # 1. Abrir la imagen desde la misma ruta del repositorio
    img = Image.open("Logotipo DINO2TECNO evolutivo.jpg")
    
    # 2. Mostrar la imagen en una ventana aparte del sistema (visor de Windows)
    img.show()
    
    print("¡Imagen abierta exitosamente en una ventana independiente!")
    
except FileNotFoundError:
    print("Error: No se encontró el archivo de imagen. Verifica el nombre y la ruta.")
