import json, requests, menus, statistics
import matplotlib.pyplot as plt
import numpy as np

nombretipos = []

m = ("¿Desea consultar otro pokemon? \n1. Si \n2. No")

def consulta(dato):
    id = menus.verif_id()
    a = requests.get("https://pokeapi.co/api/v2/pokemon/" + id + "/")
    if a.status_code != 200:
        print("No se encontro ese id, vuelve a iniciar")
        exit()
    a = json.loads(a.text)
    b = a["name"]
    c = a.get(dato) / 10
    return b, c #regresa una tupla con el nombre y el peso o altura de un pokemon


def grafica(pesoaltura, nombres, valores):
    pokemon = consulta(pesoaltura) #de consulta un pokemon
    print("El nombre del pokemon es:", pokemon[0]) #se imprime el nombre
    if pesoaltura == "weight": #decide si se imprimira el peso o la altura
        print("Y su peso es:",pokemon[1],"kgs.")
    else:
        print("Y su altura es:",pokemon[1],"mts.")
    print("\n")
    nombres.append(pokemon[0]) #se añade el nombre a una lista
    valores.append(pokemon[1]) #se añade el peso o altura a una lista
    x = menus.menupoke2(m) #se le pregunta al usuario si quiere consultar otro pokemon o graficar
    if x == 2:
        xax = np.array(nombres) #el eje x constara de nombres
        yax = np.array(valores) #el eje y constara de las alturas/pesos de los pokemon
        plt.bar(xax, yax) #se grafica
        plt.show() #se muestra
        return #termina la funcion
    else:
        grafica(pesoaltura, nombres, valores) #si se quiere seguir consultado pokemones, se llama a la funcion
        return #cuando termine la funcion, se regresa


def repeticiones(listadetipos):
    data = {}
    for tipo in listadetipos: #recorre los tipos en la lista de tipos
        if tipo not in data: #si el tipo no se encuentra en una lista
            data[tipo] = 0 #se añade al diccionario
        data[tipo] += 1 #si se encuentra, se le suma 1
    return data #regresa el diccionario con las repeticiones de cada tipo


def consultatipos():
    id = menus.verif_id()
    a = requests.get("https://pokeapi.co/api/v2/pokemon/" + id + "/")
    if a.status_code != 200:
        print("No se encontro ese id, vuelve a iniciar")
        exit()
    a = json.loads(a.text)
    print("El nombre del pokemon es:", a["name"])
    print("Y es tipo:")
    a = a.get("types")
    for elem in a:
        tipos = elem["type"]["name"]
        print("-",tipos)
        nombretipos.append(tipos)
    print("\n")
    opc = menus.menupoke2(m)
    if opc == 1:
        return (consultatipos())
    else:
        return nombretipos


def graficapay():
    listanombres = [] #lista de nombres de los pokemones vacia
    listadetipos = [] #lista de tipos vacia
    x = consultatipos() #se consultan los tipos de los pokemones, y regresa una lista
    x = repeticiones(x) #se cuenta cuantas veces se repiten, y regresa un diccionario
    for nombres, valor in x.items():
        listanombres.append(nombres) #añade los nombres del diccionario (estos siendos las llaves)
        listadetipos.append(valor) #añade el tipo del diccionario (estos siendos los valores)
    fig, ax = plt.subplots()
    ax.pie(listadetipos, labels=listanombres, autopct='%1.1f%%') #crea la figura de pay
    plt.show() #se muestra la figura
    return #termina la funcion