from typing import Optional, TypeVar, Generic

T = TypeVar('T')
class nodo(Generic[T]):
    #Representa un nodo individual para las estructuras enlazadas
    def __init__(self,dato):
        self.dato: T = dato # CARGA UTIL (Valor a guardar)
        self.siguiente: Optional['nodo[T]'] = None #Puntero al siguiente nodo que esta vacio