import random

def crear_alumnos(cantidad_de_alumnos=5):
    nombres = ['Javier', 'Pablo', 'Ramiro', 'Lucas', 'Carlos']
    apellidos = ['Saviola', 'Aimar', 'Funes Mori', 'Alario', 'Sanchez']

    alumnos = []
    for i in range(cantidad_de_alumnos):
        a = {
            'nombre': '{}, {}'.format(
                random.choice(apellidos), random.choice(nombres)),
            'padron': random.randint(90000, 100000),
            'nota': random.randint(4, 10)
        }
        alumnos.append(a)
    
    return alumnos


def imprimir_curso(lista):
    for idx, x in enumerate(lista, 1):
        print '    {pos:2}. {padron} - {nombre}: {nota}'.format(
            pos=idx, **x)


def obtener_padron(alumno):
    return alumno['padron']


def ordenar_por_padron(alumno1, alumno2):
    if alumno1['padron'] < alumno2['padron']:
        return -1
    elif alumno2['padron'] < alumno1['padron']:
        return 1
    else:
        return 0

curso = crear_alumnos()
print 'La lista tiene los alumnos:'
imprimir_curso(curso)

lista_ordenada = sorted(curso, key=obtener_padron)
print 'Y la lista ordenada por padron:'
imprimir_curso(lista_ordenada)

otra_lista_ordenada = sorted(curso, cmp=ordenar_por_padron)
print 'Y la lista ordenada por padron:'
imprimir_curso(otra_lista_ordenada)
