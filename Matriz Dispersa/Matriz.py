import os
import graphviz
import csv

class Nodo:
    #Crea los espacios para almacenar la fila, columna, valor y el puntero al siguiente nodo
    __espacios__ = "fila", "columna", "valor", "siguiente"

    def __init__(self, fila = 0, columna = 0, valor = 0, siguiente = None):
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.siguiente = siguiente
    
class Dispersa:

    def __init__(self):
        self.cabeza = None
        self.temp = None
        self.tamanio = 0
    #Verifica si la lista esta vacia o no
    def vacio(self):
        return self.tamanio == 0
    #Crea el nodo para la lista enlazada simple tomando el dato de la matriz
    def insertar_nodo(self, fila, columna, valor):

        nuevoNodo = Nodo(fila, columna, valor, None)
        #Si la lista enlazada esta vacia, inserta el nodo en la cabeza
        if self.vacio():
            self.cabeza = nuevoNodo
        else:
            self.temp.siguiente = nuevoNodo
        self.temp = nuevoNodo

        self.tamanio += 1
    #Muestra el contenido de la lista enlazada simple
    def mostrar_lista(self):
        temp = f = c = self.cabeza
        print("Valor: ")
        while temp != None:
            print(temp.valor, end = " ")
            temp = temp.siguiente
        
        print("\nPosicion de la fila: ")
        while f != None:
            print(f.fila, end = " ")
            f = f.siguiente
        
        print("\nPosicion de la columna: ")
        while c != None:
            print(c.columna, end = " ")
            c = c.siguiente
    #Funcion que genera un png con la lista enlazada de la matriz
    def graficar_nodo(self):
        g = graphviz.Digraph()
        nodo = self.cabeza
        nodo_ant = self.cabeza
        i = 0
        while nodo != None:
            g.node(str(nodo.valor))
            if i >= 1:
                g.edge(str(nodo_ant.valor), str(nodo.valor)) #Agrega la arista que apunta del nodo anterior al nodo siguiente
                nodo_ant = nodo_ant.siguiente 
            nodo = nodo.siguiente
            i += 1
        g.render('Lista grafica', format="pdf")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__=="__main__":
    opcion = 0
    disperso = Dispersa()

    while opcion != 4:
        print("TAREA 4 - MATRIZ DISPERSA")
        print("\n1) Cargar archivo CSV \n2) Insertar informacion manualmente \n3) Mostrar datos por consola \n4) Salir")
        opcion = int(input("Ingrese el numero de opcion que desea realizar: "))
        
        if opcion == 1:
            print("Aun no esta listo")
            matriz = []
            filas = 0
            with open("heart_failure_clinical_records_dataset.csv","r") as archivo:
                lector = csv.reader(archivo)
                next(lector) #Se salta la cabecera del archivo CSV
                for fila in lector:
                    #print(fila)
                    matriz.append(fila)
                #print(str(lector.line_num - 1)) 
                filas = lector.line_num - 1 #Obtiene el numero de filas
            archivo.close()
            #Recorre cada elemento en la matriz y si es distinto de cero lo inserta en un nodo
            for i in range(filas):
                for j in range(13):
                    if matriz[i][j] != 0:
                        disperso.insertar_nodo(i,j,matriz[i][j])
            disperso.graficar_nodo()
        
        elif opcion == 2:
            filas = int(input("Ingrese el numero de filas: "))
            columnas = int(input("Ingrese el numero de columnas: "))
            #Inicializamos una matriz vacia (se tratara como una lista de listas)
            matriz = []
            for i in range(filas):
                #Inicializamos una lista vacia
                fila = []
                for j in range(columnas):
                    numero = int(input(f"Ingrese el valor para la posicion [{i}][{j}]: "))
                    fila.append(numero)
                matriz.append(fila)
            #Recorre cada elemento en la matriz y si es distinto de cero lo inserta en un nodo
            for i in range(filas):
                for j in range(columnas):
                    if matriz[i][j] != 0:
                        disperso.insertar_nodo(i,j,matriz[i][j])
            disperso.graficar_nodo()
       
        elif opcion == 3:
            disperso.mostrar_lista()
        elif opcion == 4:
            print("Programa finalizado")
        else: 
            print("Opcion no valida.")
        input("Presione cualquier tecla para continuar")
        limpiar_pantalla()