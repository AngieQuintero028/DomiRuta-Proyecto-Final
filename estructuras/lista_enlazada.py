from estructuras.nodo import nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  #Apunta al primer nodo de la lista (empieza vacia)
        self.tamano = 0     #Cuenta cuantos elementos hay


    def esta_vacia(self):
        # 0(1): Retorna True si la cabeza es None (no hay elementos)
        return self.cabeza is None

    """
    este bloque len permite usar la funcion len(tu lista) para ver cuantos elementos tiene 
    de forma instantanea
    """
    
    def __len__(self):
        # 0(1): Devuelve el numero total de elementos almacenados
        return self.tamano