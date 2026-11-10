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

    def insertar_inicio(self, dato: T) -> None:
        # 0(1): Agrega un nuevo elemento al inicio
        nuevo_nodo = nodo(dato) # Creamos un nuevo vagon o nodo que guarda el dato que pasaste por parametro
        nuevo_nodo.siguiente = self.cabeza #El puntero del nuevo nodo ahora apunta a donde antes apuntaba la cabeza. asi no perdemos la lista que ya teniamos
        self.cabeza = nuevo_nodo # Convertimos el nuevo nodo ahora en la nueva cabeza
        self.tamano += 1 # Sumamos uno al contador de tamano de la lista

    def insertar_final(self, dato: T) -> None:
        # 0(1): Agrega un nuevo elemento al final usando el puntero _cola
        nuevo_nodo = nodo(dato)
        if self.esta_vacia(): # Si la lista esta vacia, el nuevo nodo es tanto el primero como el ultimo
            self.cabeza = nuevo_nodo 
            self._cola = nuevo_nodo
        else:
            self._cola.siguiente = nuevo_nodo # Si ya habia elementos, el nodo que era el ultimo ahora apunta al nuevo nodo
            self._cola = nuevo_nodo # Actualizamos la referencia cola para que el nuevo nodo sea ahora el ultimo de la fila
        self.tamano += 1 # Incrementamos el tamano total