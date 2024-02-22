import os
import graphviz

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class listaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_inicio(self, nombre, apellido, carnet):
        if self.cabeza is None:
            self.cabeza = self.cola = Nodo(nombre, apellido, carnet)
        else:
            temp = Nodo(nombre, apellido, carnet)
            temp.siguiente = self.cabeza
            self.cabeza.anterior = None
            self.cabeza = temp

    def insertar_final(self, nombre, apellido, carnet):
        if self.cabeza is None:
            self.cabeza = self.cola = Nodo(nombre, apellido, carnet)
        else:
            nuevo = Nodo(nombre, apellido, carnet)
            temp = self.cabeza
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = nuevo
            nuevo.anterior = temp

    def eliminar_valor(self, carnet):
        if self.cabeza is None:
            print("La lista esta vacia")
            return
        
        if self.cabeza.carnet == carnet:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza != None:
                self.cabeza.anterior = None
            return
        
        temp = self.cabeza
        while temp != None:
            if temp.carnet == carnet:
                break
            temp = temp.siguiente
        if temp is None:
            print("Elemento no encontrado")
            return
        if temp.siguiente != None:
                temp.anterior.siguiente = temp.siguiente
                temp.siguiente.anterior = temp.anterior
                return
        else:
            if temp.carnet == carnet:
                temp.anterior.siguiente = None

    def mostrar_lista(self):
        if self.cabeza is None:
            print("La lista esta vacia")
            return
        temp = self.cabeza
        linea = str(temp.anterior) + " <- " #La variable linea guarda en formato de string el valor None de la cabeza que apunta al anterior
        while temp.siguiente != None:
            linea += temp.carnet + " " + temp.nombre + " " + temp.apellido + " <-> " #En cada iteracion guarda los valores de cada nodo
            temp = temp.siguiente
        linea += " <-> " + temp.carnet + " " + temp.nombre + " " + temp.apellido + " -> " + str(temp.siguiente) #Guarda los valores del ultimo nodo y del valor None de la cola que apunta a siguiente
        print(linea)

# Esta funcion grafica la lista enlazada usando la libreria de Graphviz y generando la imagen de la lista
    def graficar_nodo(self):
        g = graphviz.Digraph() #Crea el grafo dirigido
        nodo_sig = self.cabeza #Nodo principal
        nodo_ant = self.cabeza #Este nodo sirve para obtener el valor del nodo anterior al principal
        i = 0
        while nodo_sig != None:
            g.node(nodo_sig.carnet) #Inserta el nodo
            if i >= 1:
                g.edge(nodo_ant.carnet, nodo_sig.carnet) #Agrega la arista que apunta del nodo anterior al nodo siguiente
                g.edge(nodo_sig.carnet, nodo_ant.carnet) #Agrega la arista que apunta del nodo siguiente al nodo anterior
                nodo_ant = nodo_ant.siguiente #El nodo principal se movera al siguiente nodo
            nodo_sig = nodo_sig.siguiente #Que el nodo principal pase al siguiente nodo
            i += 1
        g.render('lista grafica', format = "png") #Guarda la lista en formato png en la misma carpeta


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# try:
if __name__== '__main__':
    opcion = 0
    datos = listaDoble()
    while opcion != 5:
        print("1) Insertar al princio \n2) Insertar al final \n3) Eliminar por valor \n4) Mostrar lista \n5) Salir")
        opcion = int(input("Ingrese el numero de opcion que desea realizar: "))
        if opcion == 1:
            nombre = input("Ingrese un nombre: ")
            apellido = input("Ingrese un apellido: ")
            carnet = input("Ingrese el no. de carnet: ")
            datos.insertar_inicio(nombre,apellido,carnet)
            datos.graficar_nodo()
        elif opcion == 2:
            nombre = input("Ingrese un nombre: ")
            apellido = input("Ingrese un apellido: ")
            carnet = input("Ingrese el no. de carnet: ")
            datos.insertar_final(nombre,apellido,carnet)
            datos.graficar_nodo()
        elif opcion == 3:
            carnet = input("Ingrese el no. de carnet a eliminar: ")
            datos.eliminar_valor(carnet)
            datos.graficar_nodo()
        elif opcion == 4:
            datos.mostrar_lista()
        elif opcion == 5:
            print("Programa finalizado")
        else: 
            print("Opcion no valida.")
        input("Presione cualquier tecla para continuar")
        limpiar_pantalla()
# except Exception as error:
#     print(error)