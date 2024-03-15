import os
import graphviz

# La clase nodoArbol representa un nodo en un árbol binario con un valor y referencias a los nodos
# secundarios izquierdo y derecho.
class nodoArbol:

    def __init__(self, valor):

        self.valor = valor
        self.izq = None
        self.der = None

# La clase ABB representa un árbol de búsqueda binario con un nodo raíz no inicializado.
class ABB:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        self.raiz = self.insertarNodo(valor, self.raiz)
    
    def insertarNodo(self, valor, nodo):
    
        #La función `insertarNodo` inserta recursivamente un nodo con un valor dado en un árbol binario basándose en la comparación de valores.

        if (nodo == None):
            return nodoArbol(valor)
        
        else:
            if (valor < nodo.valor):
                nodo.izq = self.insertarNodo(valor, nodo.izq)

            if (valor > nodo.valor):
                nodo.der = self.insertarNodo(valor, nodo.der)
        return nodo

    def buscarNodo(self, valor, nodo):
    
        #Esta función busca recursivamente un nodo con un valor específico en un árbol binario.
        
        if nodo == None:
            return None
        else:
            if nodo.valor == valor:
                return nodo.valor
            elif valor < nodo.valor:
                return self.buscarNodo(valor, nodo.izq)
            else:
                return self.buscarNodo(valor, nodo.der)
        
    def eliminarNodo(self, valor, nodo):
        
        #La función `eliminarNodo` se utiliza para eliminar un nodo con un valor específico de una estructura de árbol binario.
        
        temp = None
        if (nodo is not None):
            if (valor < nodo.valor):
                nodo.izq, temp = self.eliminarNodo(valor, nodo.izq)

            elif (valor > nodo.valor):
                nodo.der, temp = self.eliminarNodo(valor, nodo.der)

            else:
                temp = nodo.valor
                if (nodo.izq is None):
                    nodo = nodo.der
                elif (nodo.der is None):
                    nodo = nodo.izq
                else:
                    nodo.izq, temp = self.reemplazar(nodo.izq)
                    nodo.valor = temp.valor
        return nodo, temp 
    
    def reemplazar(self, nodo):
        
        #La función `reemplazar` reemplaza recursivamente un nodo con su hijo derecho si existe, o con su hijo izquierdo si el hijo derecho es nulo.
        
        temp = None
        if (nodo.der is None):
            temp = nodo
            nodo = nodo.izq
        else:
            nodo.der, temp = self.reemplazar(nodo.der)
        return nodo, temp
    
    def inorder(self, nodo):
        
        #La función realiza de forma recursiva un recorrido en orden en un árbol binario a partir de un nodo determinado.
    
        if nodo:
            self.inorder(nodo.izq)
            print(nodo.valor)
            self.inorder(nodo.der)

    def cargarArchivo(self):
        
        #La función `cargarArchivo` lee un archivo de entrada, convierte cada línea en un número entero e inserta los valores enteros en un nodo.
    
        try:
            with open(input("Escribe la direccion en donde se encuentra el archivo: "), 'r') as archivo:
                for linea in archivo:
                    valor = int(linea)
                    self.insertar(valor)
        except (FileNotFoundError, IndexError) as error:
            print(error)

    def graficarArbol(self, nodo):
        
        #La función `graficarArbol` genera una representación gráfica de un árbol binario usando la biblioteca Graphviz en Python.
        
        g = graphviz.Digraph()
        g.node(str(nodo.valor))
        
        def insertar_aristas(nodo):
            
            #La función `insertar_aristas` inserta recursivamente bordes entre nodos en una representación de gráfico de árbol binario y representa el gráfico como una imagen PNG.
            
            if nodo.izq:
                g.node(str(nodo.izq.valor))
                g.edge(str(nodo.valor), str(nodo.izq.valor))
                insertar_aristas(nodo.izq)
            if nodo.der:
                g.node(str(nodo.der.valor))
                g.edge(str(nodo.valor), str(nodo.der.valor))
                insertar_aristas(nodo.der)
        insertar_aristas(nodo)
        g.render('Grafica Arbol', format = "png")


def limpiar_pantalla():
    
    #La función `limpiar_pantalla` limpia la pantalla de la consola en Python.
    
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__== '__main__':
    opcion = 0
    dato = ABB()
    while opcion != 6:
        print("1) Insertar nodo \n2) Buscar nodo \n3) Eliminar por valor \n4) Cargar desde Archivo \n5) Recorrido Inorder \n6) Salir")
        opcion = int(input("Ingrese el numero de opcion que desea realizar: "))
        if opcion == 1:
            valor = int(input("Ingrese un numero entero: "))
            dato.insertar(valor)
            dato.graficarArbol(dato.raiz)
        elif opcion == 2:
            valor = int(input("Ingrese el numero a buscar: "))
            print(dato.buscarNodo(valor, dato.raiz))
        elif opcion == 3:
            valor = int(input("Ingrese el numero a eliminar: "))
            dato.eliminarNodo(valor, dato.raiz)
            dato.graficarArbol(dato.raiz)
        elif opcion == 4:
            dato.cargarArchivo()
            dato.graficarArbol(dato.raiz)
        elif opcion == 5:
            dato.inorder(dato.raiz)
        elif opcion == 6:
            print("Programa finalizado")
        else: 
            print("Opcion no valida.")
        input("Presione cualquier tecla para continuar")
        limpiar_pantalla()        