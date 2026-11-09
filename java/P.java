public class P 
{
    public static void main(String[] args) {
        System.out.println("Hola, mundo!");
        eliminarDuplicados();
       

    }
    public static void eliminarDuplicados () {
        Listas lista = new Listas();
        lista.insertarEnPosicion(10, 0);
        lista.insertarEnPosicion(20, 1);
        lista.insertarEnPosicion(10, 2);
        lista.insertarEnPosicion(30, 3);
        lista.insertarEnPosicion(20, 4);
        lista.imprimirLista();
        lista.elimnarDuplicados();
        lista.imprimirLista();
    }
    public static void insertarEnPosicion() {
        Listas lista = new Listas();
       lista.insertarEnPosicion(19, 0);
        lista.insertarEnPosicion(21, 1);
        lista.insertarEnPosicion(34, 2);
        lista.imprimirLista();
        // Insertar los datos de la Prueba de escritorio
        lista.insertarEnPosicion(57, 0);
        lista.insertarEnPosicion(45, 4);
        lista.imprimirLista();
    }
}