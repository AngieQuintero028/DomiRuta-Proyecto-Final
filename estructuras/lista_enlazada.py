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

    def obtener(self, pos(int)) -> T:
        # 0(n): Retorna el dato en la posicion indicada. Lanza IndexError si no es valida
        if pos <0 or pos >= self.tamano: #Validamos que la posicion pedida no sea negativa ni mayor o igual al tamano total de la lista
            raise IndexError("La posicion esta fuera de rango en la lista enlazada")

        actual = self.cabeza
        for _ in range(pos): # Damos tantos pasos hacia adelante como indique la posicion para llegar al nodo exacto
            actual = actual.siguiente #Type: ignore
        return actual.dato # type: ignore Devolvemos el valor que esta guardado en ese nodo

    def buscar(self, dato: T) -> int:
        # 0(n): Retorna la posicion de la primera coincidencia del dato o -1 si no existe
        actual = self.cabeza #Arrancamos desde el inicio con el contador de posiciones en 0
        pos = 0
        while actual is not None: #Recorremos nodo por nodo mientras existan elementos
            if actual.dato == dato: # Si el dato del nodo actual coincide con lo que buscamos, devolvemos de inmediato la posicion
                return pos
            actual = actual.siguiente # Si no es, avanzamos al siguiente nodo y sumamos uno a la posicion
            pos += 1
        return -1 # Si el ciclo termina y no encontramos nada, devolvemos -1