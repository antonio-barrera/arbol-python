from clases.Nodo import *

class Arbol:
    def __init__(self):
        self.__raiz = None

    def insertar(self, dato, padre = None):
        if padre == None:
            if self.__raiz == None:
                self.__raiz = Nodo(dato)
            else:
                self.insertar(dato, self.__raiz)
        else:
            if dato > padre.dato:
                if padre.derecho == None:
                    padre.derecho = Nodo(dato)
                else:
                    if padre.izquierdo == None:
                        padre.izquierdo = Nodo(dato)
                    else:
                        self.insertar(dato, padre.izquierdo)
