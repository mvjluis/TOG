import glob
from random import shuffle
from skimage.transform import resize
from skimage import io
import numpy as np
import h5py


def main():
    # Obtener ruta deseada y el ancho y alto para redimensionar
    ruta = input("Ruta del folder con las imagenes a redimensionar: ")
    alto = int(input("Altura deseada: "))
    ancho = int(input("Ancho deseado: "))
    ruta_hdf5 = ruta.strip('\/')+('\/')
    ruta = ruta.strip('\/')+('\/*.jpg')
    print("Ruta: ", ruta)
    archivos = glob.glob(ruta)
    print(archivos)
    # crear archivo h5py
    etiquetas = []
    
    # Sobre escribe las imagenes
    for archivo in archivos:
        if 'tree' in archivo:
            etiquetas.append(1)
        else:
            etiquetas.append(0)

    datos = list(zip(archivos,etiquetas))
    shuffle(datos)

    archivos, etiquetas = zip(*datos)

    datos_dim = (len(archivos), alto, ancho)


    f=h5py.File(ruta_hdf5+'dataset.hdf5', mode='w')
    f.create_dataset("images", datos_dim, np.uint8)
    f.create_dataset("labels", (len(etiquetas),), np.uint8)
    f["labels"][...]=etiquetas

    for i in range(len(archivos)):
        archivo = archivos[i]
        imagen = io.imread(archivo)
        imagen = resize(imagen, (alto, ancho), anti_aliasing=True)
        imagen = 255*imagen
        imagen = imagen.astype(np.uint8)
        print(imagen.max())
        io.imsave(archivo, imagen)
        imagen = imagen[:,:,1] # nos quedamos con escala de grises del canal verde
        f["images"][i, ...] = imagen[None]
            
    f.close()    
main()
