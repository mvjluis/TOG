import glob
from skimage.transform import resize
from skimage import io
import json

#Leer archivos .json en carpeta /dataset/etiquetas
def leer_json(ruta):
    ruta = ruta.strip('\/')+('\/*.json')
    archivos = glob.glob(ruta)
    return archivos

def obtener_etiquetas(archivo):
    with open(archivo, 'r') as arch_json:
        nombre = ''
        clases = []
        cajas = []
        punto = {}
        puntos = []

        datos = json.load(arch_json)
        nombre = archivo.split('.')[:2]
        # nombre de archivo: archivo.split('.')[:2]
        # clase: objects --> classTitle
        # caja delimitadora: objects --> points --> exterior
        objetos = datos['objects']
        for objeto in objetos:
            clases.append(objeto['classTitle'])
            punto = objeto['points']
            puntos.append(punto['exterior'])
    return [nombre, clases, puntos]

def extraer_objetos(etiqueta, ruta_e, ruta_s, cont1, cont2):
    #revisar si existen clases
    if len(etiqueta[1])==0:
        return cont1, cont2
    num_arbol = cont1
    num_otro = cont2
    ruta_a = etiqueta[0] # Arreglo [ruta, formato]
    clases = etiqueta[1] # Arreglo [clase1, clase2, etc.]
    puntos = etiqueta[2] # Arreglo [[[X1, Y1],[X2, Y2]], ...]
    
    # abrir imagen
    rutas = ruta_a[0].split('\\')[-1]
    print(rutas)
    imagen = io.imread(ruta_e+rutas+'.'+ruta_a[1])

    # por cada etiqueta extraer la imagen de interes y guardar imagen
    for i in range(len(clases)):
        clase = clases[i]
        punto = puntos[i]
        x1 = punto[0][0]
        x2 = punto[1][0]
        y1 = punto[0][1]
        y2 = punto[1][1]
        # cortar region de interes
        imagen_rec = imagen[y1:y2, x1:x2]
        if clase == "tree":
            num = num_arbol
            num_arbol += 1
        else:
            num = num_otro
            num_otro += 1
            
        # Guardar imagen
        io.imsave(ruta_s+clase+'_'+str(num)+'.jpg', imagen_rec)

    return num_arbol, num_otro
    

def main():
    # Obtener lista de archivos json
    ruta_entrada = "\\dataset\\etiquetas\\"
    #ruta_entrada = input("Ruta del folder con los archivos .json: ")
    # ruta imagenenes
    ruta_im = "C:\\Users\\mvjlu\\Documents\\02_Maestria\\02_2ndoSemestre\\022_ProgramacionAnalisisDatos\\Plantillas\\Proyecto_PAD\\Scripts\\00_Etiquetado\\dataset\\imagenes\\"
    #ruta_im = input("Ruta del folder las imagenes a extraer los objetos de interes: ")
    # Ruta de  salida
    ruta_salida = "C:\\Users\\mvjlu\\Documents\\02_Maestria\\02_2ndoSemestre\\022_ProgramacionAnalisisDatos\\Plantillas\\Proyecto_PAD\\Scripts\\00_Etiquetado\\dataset\\proc_imagenes\\"
    #ruta_salida = input("Ruta del folder con las imagenes de interes etiquetadas: ")

    # Leer archivos con las etiquetas y las regiones de interés
    archivos = leer_json(ruta_entrada)
    arb_cont = 0
    ot_cont = 0
    etiquetas = []
    for archivo in archivos:
        etiquetas.append(obtener_etiquetas(archivo))
    print(etiquetas)

    # Cortar imagenes de interes
    for etiqueta in etiquetas:
        arb_cont, ot_cont = extraer_objetos(etiqueta, ruta_im, ruta_salida, arb_cont, ot_cont)

main()
