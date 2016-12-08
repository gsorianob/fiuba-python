#encoding: utf8

class Nodo(object):
    
    def __init__(self, valor, siguiente=None):
        self.siguiente = siguiente
        self.valor = valor


class Pila(object):

    def __init__(self):
        self.primero = None
        self.tamanio = 0

    def __str__(self):
        pila = '<Pila: '
        siguiente = self.primero
        while siguiente:
            pila += '{} | '.format(siguiente.valor)
            siguiente = siguiente.siguiente

        pila +='>'
        return pila 

    def apilar(self, elemento):
        """Guarda el elemento a insertar al final de la pila"""
        nodo = Nodo(elemento, self.primero)
        self.primero = nodo
        self.tamanio += 1

    def desapilar(self):
        """Quita y retorna último elemento insertado en la pila"""
        nodo = self.primero
        try:
            elemento = nodo.valor
        except AttributeError:
            raise Exception(u'No se puede desapilar elementos de una pila vacía')
        self.primero = nodo.siguiente
        self.tamanio -= 1

        return elemento

    def esta_vacia(self):
        """Devuelve True si la pila no contiene elementos y 
        False en el caso de que tenga al menos un elemento"""
        return not self.tamanio


class Cola(object):

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def __str__(self):
        cola = '<Cola: | '
        siguiente = self.primero
        while siguiente:
            cola += '{} | '.format(siguiente.valor)
            siguiente = siguiente.siguiente

        cola +='>'
        return cola 

    def encolar(self, elemento):
        """Guarda el elemento a insertar al final de la cola"""
        nodo = Nodo(elemento)
        self.tamanio += 1
        if not self.primero:
            self.primero = nodo
        else:
            self.ultimo.siguiente = nodo

        self.ultimo = nodo


    def desencolar(self):
        """Quita y retorna el primer elemento insertado"""
        nodo = self.primero
        try:
            elemento = nodo.valor
        except AttributeError:
            raise Exception(u'No se puede desencolar más elementos')
        self.primero = nodo.siguiente
        self.tamanio -= 1

        return elemento

    def esta_vacia(self):
        """Devuelve True si la cola no contiene elementos y 
        False en el caso de que tenga al menos un elemento"""
        return not self.tamanio


class Lista(object):

    def __init__(self):
        self.primero = None
        self.cursor = None
        self.tamanio = 0

    def __str__(self):
        lista = '<Lista: '
        siguiente = self.primero
        while siguiente:
            lista += '{} | '.format(siguiente.valor)
            siguiente = siguiente.siguiente

        lista +='>'
        return lista
    
    def obtener_elemento(self):
        """Retorna el elemento de la posición actual"""
        try:
            return self.cursor.valor
        except AttributeError:
            raise Exception(u'La lista se encuentra vacía')

    def insertar_siguiente(self, elemento):
        """Guarda el elemento a insertar en la posición actual"""
        nodo = Nodo(elemento)
        if not self.primero:
            self.primero = nodo
        else:
            nodo.siguiente = self.cursor.siguiente
            self.cursor.siguiente = nodo
        
        self.cursor = nodo
        self.tamanio += 1

    def eliminar(self, posicion):
        """Elimina el elemento de la posición indicada"""
        if posicion > self.tamanio:
            msg = u'Se quiere borrar la posición {0} y la lista sólo tiene' \
                  u' {1} elementos'
            raise Exception(msg.format(posicion, self.tamanio))
        elif posicion == 1:
            nodo = self.primero
            self.primero = self.primero.siguiente
        else:
            nodo_anterior = self.primero
            pos_nodo = 2
            while pos_nodo < posicion:
                nodo_anterior = nodo_anterior.siguiente
                pos_nodo += 1 

            nodo = nodo_anterior.siguiente
            
            if self.cursor == nodo_anterior.siguiente:
                self.cursor = nodo_anterior.siguiente.siguiente

            if nodo_anterior.siguiente:
                nodo_anterior.siguiente = nodo_anterior.siguiente.siguiente
        
        self.tamanio -= 1
        return nodo
    
    def ir_al_primero(self):
        """Posiciona el cursor apuntando al primer elemento de la lista"""
        self.cursor = self.primero

    def siguiente(self):
        """Avanza el cursor al siguiente elemento de la lista"""
        try:
            self.cursor = self.cursor.siguiente
        except AttributeError:
            msg = u'Error: La lista tiene {0.tamanio} elementos y quiere ' \
                  u'acceder a la posición {1}'
            pos = self.tamanio + 1 
            raise IndexError(msg.format(self, pos))

    def esta_vacia(self):
        """Devuelve True si la cola no contiene elementos y 
        False en el caso de que tenga al menos un elemento"""
        return not self.tamanio
