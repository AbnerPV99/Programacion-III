import os

class Nodo: 
    def __init__(self, clave, valor): 
        self.clave = clave 
        self.valor = valor 
        self.siguiente = None
  
  
class TablaHash: 
    def __init__(self, capacidad): 
        self.capacidad = capacidad 
        self.tamanio = 0
        self.tabla = [None] * capacidad 
  
    def hash(self, clave): 
        return hash(clave) % self.capacidad 
  
    def insertar(self, clave, valor): 
        indice = self.hash(clave) 
  
        if (self.tabla[indice] is None): 
            self.tabla[indice] = Nodo(clave, valor) 
            self.tamanio += 1
        else: 
            actual = self.tabla[indice] 
            while actual: 
                if (actual.clave == clave): 
                    actual.valor = valor 
                    return
                actual = actual.siguiente
            nuevoNodo = Nodo(clave, valor) 
            nuevoNodo.siguiente = self.tabla[indice] 
            self.tabla[indice] = nuevoNodo
            self.tamanio += 1
  
    def buscar(self, clave): 
        indice = self.hash(clave) 
  
        actual = self.tabla[indice] 
        while actual: 
            if (actual.clave == clave): 
                return actual.valor, actual.clave
            actual = actual.siguiente
        else:
            print("Valor no encontrado")
  
        raise KeyError(clave) 
  
    def eliminar(self, clave): 
        indice = self.hash(clave) 
  
        anterior = None
        actual = self.tabla[indice] 
  
        while actual: 
            if (actual.clave == clave): 
                if anterior: 
                    anterior.siguiente = actual.siguiente
                else: 
                    self.tabla[indice] = actual.siguiente
                self.tamanio -= 1
                return
            anterior = actual 
            actual = actual.siguiente
  
        raise KeyError(clave) 
  
    def __len__(self): 
        return self.tamanio 
  
    def __contains__(self, clave): 
        try: 
            self.buscar(clave) 
            return True
        except KeyError: 
            return False
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__=="__main__":
    opcion = 0
    th = TablaHash(100)

    while opcion != 4:
        print("HOJA DE TRABAJO 8")
        print("\n1) Cargar archivo CSV \n2) Insertar informacion manualmente \n3) Buscar por clave \n4) Eliminar \n5) Salir")
        opcion = int(input("Ingrese el numero de opcion que desea realizar: "))
        
        if opcion == 1:
            print("No esta listo")
        elif opcion == 2:
            clave = input("Ingrese su clave: ")
            valor = int(input("Ingrese su numero de valor a insertar: "))
            th.insertar(clave, valor)
        elif opcion == 3:
            clave = input("Ingrese la clave a buscar: ")
            print(th.buscar(clave))
        elif opcion == 4:
            clave = input("Ingrese su clave a eliminar: ")
            th.eliminar(clave)
        elif opcion == 5:
            print("Programa finalizado")
        else: 
            print("Opcion no valida.")
        input("Presione cualquier tecla para continuar")
        limpiar_pantalla()
