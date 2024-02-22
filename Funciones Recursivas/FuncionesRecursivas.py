import os

def convertir_a_binario(numero):
    if (numero == 0):
        return " "
    return convertir_a_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero):
    if (numero < 10):
        return 1
    else:
        return contar_digitos(numero // 10) + 1

def raiz_cuadrada_entera(numero):
    valor = numero
    print(calcular_raiz_cuadrada(0, valor, valor))

def calcular_raiz_cuadrada(primero, ultimo, numero):
    if (primero <= ultimo):
        medio = (primero + ultimo) // 2
        if ((medio * medio <= numero) and ((medio + 1) * (medio + 1) > numero)):
            return medio
        elif (medio * medio < numero):
            return calcular_raiz_cuadrada(medio + 1, ultimo, numero)
        else:
            return calcular_raiz_cuadrada(primero, medio - 1, numero)
    return primero

def convertir_a_decimal(romano):
    diccionario = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if (len(romano) == 1):
        return diccionario[romano]
    
    elif (diccionario[romano[0]] < diccionario[romano[1]] and len(romano) == 2):
        return diccionario[romano[1]]-diccionario[romano[0]]
    
    else:
        return diccionario[romano[0]] + convertir_a_decimal(romano[1:])
    

def suma_numero_enteros(numero):
    if (numero == 1):
        return 1
    else:
        return suma_numero_enteros(numero - 1) + numero
    
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
if __name__== '__main__':
    opcion = 0
    while opcion != 6:
        print("1) Convertir a Binario \n2) Contar Digitos \n3) Raiz Cuadrada Entera \n4) Convertir a Decimal desde Romano \n5) Suma de Numeros Enteros \n6) Salir")
        opcion = int(input("Ingrese el numero de opcion que desea realizar: "))
        if opcion == 1:
            numero = int(input("Ingrese el numero decimal a convertir: "))
            print(convertir_a_binario(numero))
        elif opcion == 2:
            numero = int(input("Ingrese el numero a contar sus digitos: "))
            print(contar_digitos(numero))
        elif opcion == 3:
            numero = int(input("Ingrese el numero para calcular su raiz cuadrada entera: "))
            raiz_cuadrada_entera(numero)
        elif opcion == 4:
            romano = input("Ingrese el numero romano a convertir: ")
            print(convertir_a_decimal(romano))
        elif opcion == 5:
            numero = int(input("Ingrese el numero a sumar: "))
            print(suma_numero_enteros(numero))
        elif opcion == 6:
            print("Programa finalizado")
        else: 
            print("Opcion no valida.")
        input("Presione cualquier tecla para continuar")
        limpiar_pantalla()