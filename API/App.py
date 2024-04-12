from flask import Flask, request, jsonify
import graphviz
import csv

app = Flask(__name__)

class nodoArbol:

    def __init__(self, valor):

        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 0

# La clase AVL representa un árbol AVL con un nodo raíz no inicializado.
class AVL:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        self.raiz = self.insertarNodo(valor, self.raiz)
        #self.graficarArbol(self.raiz)
    
    def insertarNodo(self, valor, nodo):
    
        #La función `insertarNodo` inserta recursivamente un nodo con un valor dado en un árbol binario basándose en la comparación de valores.

        if (nodo == None):
            return nodoArbol(valor)
        
        else:
            if (valor < nodo.valor):
                nodo.izq = self.insertarNodo(valor, nodo.izq)

            if (valor > nodo.valor):
                nodo.der = self.insertarNodo(valor, nodo.der)
       
        self._balancear(valor, nodo)
        return nodo

    def buscar(self, valor):
        return self.buscarNodo(valor, self.raiz)

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

    def _balancear(self, valor, nodo):

        nodo.altura = 1 + max(self._get_height(nodo.izq), self._get_height(nodo.der))
        balance = self._get_balance(nodo)

        # Caso de rotación simple a la derecha
        if balance > 1 and valor < nodo.izq.valor:
            return self._rotate_right(nodo)

        # Caso de rotación simple a la izquierda
        if balance < -1 and valor > nodo.der.valor:
            return self._rotate_left(nodo)

        # Caso de rotación doble a la derecha-izquierda
        if balance > 1 and valor > nodo.izq.valor:
            nodo.izq = self._rotate_left(nodo.izq)
            return self._rotate_right(nodo)

        # Caso de rotación doble a la izquierda-derecha
        if balance < -1 and valor < nodo.der.valor:
            nodo.der = self._rotate_right(nodo.der)
            return self._rotate_left(nodo)

    def _get_height(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_height(nodo.izq) - self._get_height(nodo.der)

    def _rotate_right(self, z):
        y = z.izq
        T3 = y.der

        y.der = z
        z.izq = T3

        z.altura = 1 + max(self._get_height(z.izq), self._get_height(z.der))
        y.altura = 1 + max(self._get_height(y.izq), self._get_height(y.der))

        return y

    def _rotate_left(self, z):
        y = z.der
        T2 = y.izq

        y.izq = z
        z.der = T2

        z.altura = 1 + max(self._get_height(z.izq), self._get_height(z.der))
        y.altura = 1 + max(self._get_height(y.izq), self._get_height(y.der))

        return y
    
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

    def leer_csv(self):
        with open('./Air_Quality.csv', 'r') as csvfile:
            lector_csv = csv.DictReader(csvfile)
            
            next(lector_csv)
            
            for fila in lector_csv:
                valor = int(fila['Unique ID'])
                self.insertar(valor)

arbol = AVL()
grupo = {
    "Nombre" : "Abner Andres Perez Villatoro",
    "Carne:" : "9490-17-11829",
    "Contribuciones" : "Desarrollo de la API"
}

@app.route("/")
def root():
    return "Hoja de Trabajo 4"

@app.route("/cargar", methods=["GET"])
def cargar_csv():
    arbol.leer_csv()
    return jsonify({"Mensaje" : "CSV cargado exitosamente"})

@app.route("/insertar", methods=["GET", "POST"])
def insertar_nodo():
    if request.method == "GET":
        return jsonify({"Mensaje" : "GET recibido"})
    elif request.method == "POST":
        dato = request.json
        valor = dato.get("valor")
        if valor is None:
            return jsonify({"Error":"El valor no fue ingresado"}), 400
        arbol.insertar(valor)
        return jsonify({"Mensaje":"Nodo insertado exitosamente"}), 200

@app.route("/buscar", methods=["GET", "POST"])
def buscar_nodo():
    if request.method == "GET":
        return jsonify({"Mensaje" : "GET recibido"})
    elif request.method == "POST":
        dato = request.json
        valor = dato.get("valor")
        if valor is None:
            return jsonify({"Error":"El valor no fue ingresado"}), 400
        else:
            temp = arbol.buscar(valor)
            if temp == valor:
                return jsonify({"Mensaje":"Nodo encontrado"}), 200
            else:
                return jsonify({"Mensaje","Nodo no encontrado"}), 404

@app.route("/mostrar", methods=["GET"])
def mostrar():
    return jsonify(grupo)

if __name__=="__main__":
    app.run(debug=True)