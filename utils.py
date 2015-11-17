# encoding: utf8
import pickle

def guardar_en_archivo(archivo, contenido):
    """Guarda lo que le pasen como segundo parámetro en el archivo 
    que recibe como primer parámetro.
    El parámetro llamado archivo tiene que estar abieto en modo 
    binario y para escritura (wb)
    """
    pickler = pickle.Pickler(archivo)
    pickler.dump(contenido)


def leer_desde_archivo(archivo):
    """Lee del archivo archivo un registro y lo retorna junto con una
    variable booleana que indica si llegó al fin de archivo o no.
    El parámetro llamado archivo tiene que estar abieto en modo 
    binario y para lectura (rb).
    Si se intenta leer más allá del fin de archivo, data valdrá None
    y fin_de_archivo será True. En cualquier otro caso fin_de_archivo
    será False.
    """
    try:
        data = pickle.load(archivo)
        fin_de_archivo = False
    except EOFError:
        data = None
        fin_de_archivo = True
    return data, fin_de_archivo

