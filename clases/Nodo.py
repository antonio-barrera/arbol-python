class Nodo:
    def __init__(self, dato, izquierdo = None, derecho = None):
        self.__dato = dato
        self.__izquierdo = izquierdo
        self.__derecho = derecho

    def __get_dato(self):
        return self.__dato

    def __get_izquierdo(self):
        return self.__izquierdo

    def __get_derecho(self):
        return self.__derecho

    def __set_izquierdo(self, izquierdo):
        self.__izquierdo = izquierdo

    def __set_derecho(self, derecho):
        self.__derecho = derecho

    dato = property(fget = __get_dato)

    izquierdo = property(fget = __get_izquierdo, fset = __set_izquierdo)

    derecho = property(fget = __get_derecho, fset = __set_derecho)
