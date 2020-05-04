from os import listdir
from os.path import isfile, join
from PIL import Image

def ls(ruta="."):
    return [(join(ruta,arch)) for arch in listdir(ruta) if isfile(join(ruta,arch))]

def main():
    archivos = list()
    ruta = input("Ruta de los archivos a listar: ")
    archivos = ls(ruta)
    #print(archivos)
    for archivo in archivos:
        image = Image.open(archivo)
        image = image.resize((64,64))
        image.save(archivo)
main()