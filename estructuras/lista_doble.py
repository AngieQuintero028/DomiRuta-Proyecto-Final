def insertar_inicio(self, dato):
        """
        Agrega un nodo al comienzo de la lista.
        El nodo nuevo se conecta con la cabeza actual. Si la lista ya tenía
        nodos, actualizamos también el enlace hacia atrás. Después, el nodo
        nuevo pasa a ser la cabeza y, si era el primer elemento, también la cola.
        """
        # Creamos un nodo para guardar el dato.
        nuevo_nodo = NodoDoble(dato)

        # El siguiente del nodo nuevo será la cabeza que ya teníamos.
        nuevo_nodo.siguiente = self.cabeza

        # Si había una cabeza, hacemos que su anterior sea el nodo nuevo.
        if self.cabeza is not None:
            self.cabeza.anterior = nuevo_nodo

        # El nodo nuevo queda como la primera posición de la lista.
        self.cabeza = nuevo_nodo

        # Si la lista estaba vacía, el nodo nuevo también es el último.
        if self.cola is None:
            self.cola = nuevo_nodo

        # Registramos que ahora hay un nodo más.
        self.tamano += 1

def insertar_final(self, dato):
        """
        Agrega un nodo al final de la lista.
        El nodo nuevo se conecta con la cola actual. Si la lista ya tenía
        nodos, actualizamos también el enlace hacia adelante. Después, el nodo
        nuevo pasa a ser la cola y, si era el único elemento, también la cabeza.
        """
        # Creamos un nodo para guardar el dato.
        nuevo_nodo = NodoDoble(dato)

        # El anterior del nodo nuevo será la cola que ya teníamos.
        nuevo_nodo.anterior = self.cola

        # Si había una cola, hacemos que el siguiente sea el nodo nuevo.
        if self.cola is not None:
            self.cola.siguiente = nuevo_nodo

        # El nodo nuevo queda como la última posición de la lista.
        self.cola = nuevo_nodo

        # Si la lista estaba vacía, el nodo nuevo también es el primero.
        if self.cabeza is None:
            self.cabeza = nuevo_nodo

        # Registramos que ahora hay un nodo más.
        self.tamano += 1

def obtener(self, pos):
        """Devuelve el dato que está en la posición indicada."""
        # No permitimos posiciones negativas ni posiciones fuera de la lista.
        if pos < 0 or pos >= self.tamano:
            raise IndexError("Posición fuera de rango")

        # Empezamos por el primer nodo.
        actual = self.cabeza

        # Avanzamos tantas veces como indique la posición.
        for _ in range(pos):
            actual = actual.siguiente

        # Devolvemos el dato del nodo encontrado.
        assert actual is not None
        return actual.dato

def buscar(self, dato):
        """
        Busca el dato en la lista y devuelve la posición de la primera coincidencia.
        Si no se encuentra, devuelve -1.
        """
        actual = self.cabeza
        pos = 0

        # Recorremos la lista hasta encontrar el dato o llegar al final.
        while actual is not None:
            if actual.dato == dato:
                return pos
            actual = actual.siguiente
            pos += 1

        # Si llegamos aquí, no encontramos el dato.
        return -1

def imprimir_reversa(self):
        """
        Imprime los elementos de la lista desde la cola hasta la cabeza.
        """
        actual = self.cola
        valores = []
        while actual is not None:
            valores.append(actual.dato)
            actual = actual.anterior
        print("<-".join(map(str, valores)))