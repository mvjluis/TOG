from os import listdir
from os.path import isfile, join

def ls(ruta="."):
    return [arch for arch in listdir(ruta) if isfile(join(ruta,arch))]

def main():
    archivos = list()
    ruta = input("Ruta de los archivos a listar: ")
    archivos = ls(ruta)
    with open(ruta+"\\data.csv", "w") as data:
        for archivo in archivos:
            data.write(archivo+"\n")

main()