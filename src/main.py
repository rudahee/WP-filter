import argparse, os, sys, time
from PIL import Image

def get_arguments():
    # Este metodo se dedica a gestionar/parsear los argumentos del script.
    parser = argparse.ArgumentParser(description="[!] HELP FOR USE [!]  \n\n")
    parser.add_argument("-i", "--input", nargs=1, help=" Source of folder with images WITHOUT FINAL /")
    parser.add_argument("-o", "--output", nargs=1, help=" Destiny of folder with images WITHOUT FINAL /")
    parser.add_argument("-x", "--xaxis", nargs=1, help=" x-axis Size")
    parser.add_argument("-y", "--yaxis", nargs=1, help=" y-axis Size")
    parser.add_argument("-t", "--time", nargs=1, help=" Time for each copy, 0 for no slowdown.")
    args = parser.parse_args()

    return args

def compareSize(sizeImage, x, y): 
    # Este metodo compara el tamaño de imagen que estamos buscando
    # con el tamaño de la imagen real.
    if int(x) == sizeImage[0]:
        if int(y) == sizeImage[1]:
            return True
    return False

def getSize(path):
    # Este metodo es responsable de cargar y obtener el tamaño de la imagen
    try:
        image = Image.open(path)
        return image.size
    except:
        print("[/!!!\] No se ha podido cargar la imagen!")
        return (0,0)

def searchImages(pathInput, x, y, slow, pathOutput):
    # Buscamos en directorios y subdirectorios
    # todos los archivos donde se encuentren las imagenes.

    for file in os.listdir(pathInput):
        if slow > 0:
            time.sleep(slow)
        if os.path.isdir(pathInput + "/" + str(file)):
            searchImages(pathInput + "/" + str(file), x, y, slow, pathOutput)
        elif os.path.isfile(pathInput + "/" + str(file)):
            if compareSize(getSize(pathInput + "/" + str(file)), x, y):
                print('[->]' + str(file))
                os.popen('cp ' + pathInput + '/' + str(file) + " " + pathOutput + '/' + str(file)) 
            else:
                print('[X]' + str(file))
                

if __name__ == '__main__':
    # Metodo principal donde gestionamos los argumentos y cargamos el metodo para buscar la imagen.
    print(sys.argv)    
    options = get_arguments()
    searchImages(options.input[0], int(options.xaxis[0]), int(options.yaxis[0]), int(options.time[0]), options.output[0])