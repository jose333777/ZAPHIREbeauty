public class Listas {
    Nodo head;

    /**
     * Elimina los nodos duplicados de la lista enlazada.
     * sin importar si son elementos continuos o no.
     */
    public void elimnarDuplicados() {
        if (head == null) {
            return;
        }

        Nodo actual = head;
        Nodo recorrido = head;
        while (actual != null && actual.siguiente != null) {
            recorrido = actual;
            while (recorrido.siguiente != null) {
                if (actual.dato == recorrido.siguiente.dato) {
                    recorrido.siguiente = recorrido.siguiente.siguiente;
                } else {
                    recorrido = recorrido.siguiente;
                }
            }
            if (actual.dato == actual.siguiente.dato) {
                actual.siguiente = actual.siguiente.siguiente;
            } else {
                actual = actual.siguiente;
            }

        }
    }

    public void insertarEnPosicion(int dato, int posicion) {
        Nodo nuevoNodo = new Nodo(dato);

        if (posicion == 0) {
            nuevoNodo.siguiente = head;
            head = nuevoNodo;
            return;
        }

        Nodo actual = head;
        for (int i = 0; i < posicion - 1; i++) {
            if (actual == null) {
                throw new IndexOutOfBoundsException("Posición fuera de rango");
            }
            actual = actual.siguiente;
        }

        nuevoNodo.siguiente = actual.siguiente;
        actual.siguiente = nuevoNodo;
    }

    public void imprimirLista() {
        Nodo actual = head;
        while (actual != null) {
            System.out.print(actual.dato + " -> ");
            actual = actual.siguiente;
        }
        System.out.println("null");
    }
}
