import requests, json, statistics, menus, guardadoh, graficos
nombre_tipos = []

def consultatipos(nombre_tipos):
    id = menus.verif_id()
    a = requests.get("https://pokeapi.co/api/v2/pokemon/"+id+"/")#se consulta el pokemon deseado
    if a.status_code != 200:
        print("No se encontro ese id, vuelve a iniciar")
        exit()
    a = json.loads(a.text)
    print("El nombre del pokemon es:",a["name"])
    a = a.get("types") #de la consulta, obtenemos un diccionario con los tipos
    for elem in a:
        print("Y es tipo:")
        tipos = elem["type"]["name"] #se imprimen los tipos
        print(tipos)
        nombre_tipos.append(tipos) #se añaden los tipos a una lista
    print("\n")
    m = "¿Desea consultar otro pokemon? \n1. Si \n2. No\n" #se le pregunta al usuario si quiere consultar otro pokemon
    opc = menus.menupoke2(m)
    if opc == 1:
        return(consultatipos(nombre_tipos)) #si se consulta otro pokemon, solo se hace otra llamada a la funcion
    else:
        return nombre_tipos #si termina la consulta, se regresa la lista con los tipos

def sumatotal(sumas, pesoaltura):
    id = menus.verif_id()
    a = requests.get("https://pokeapi.co/api/v2/pokemon/"+id+"/")
    if a.status_code != 200:
        print("No se encontro ese id, vuelve a iniciar")
        exit()
    a = json.loads(a.text)
    print("El nombre del pokemon es:", a["name"],"\n") #se imprime el nombre del pokemon
    if pesoaltura == "weight": #decide si se imprimira el peso o la altura
        print("Su peso es:",(a["weight"]/10)) #Se imprime el peso del pokemon
    else:
        print("Su altura es:",(a["height"]/10)) #se imprime la altura del pokemon
    print("\n")
    a = a.get(pesoaltura)
    a = a / 10
    sumas.append(a) #se añade el peso o la altura a la lista
    m = "¿Desea consultar otro pokemon? 1. Si \n2. No\n"
    opc = menus.menupoke2(m) #se le pregunta al usuario si quiere consultar otro pokemon
    if opc == 1:
        return sumatotal(sumas, pesoaltura) #en caso de consultar otro, solo se llama a la funcion
    else:
        return sumas #cuando termine, se regresa la lista de pesos o alturas

def promedio(pesoaltura):
    suma = []
    valor = sumatotal(suma, pesoaltura)
    prom = statistics.mean(valor) #se calculo el promedio con el modulo statistics
    return prom

def moda():
    type = []
    tipos = consultatipos(type)
    data = {}
    valormax = 0
    moda = None
    for string in tipos: #va consultando cada string en una lista de tipos
        if string not in data:
            data[string] = 0 #si el string no esta en el diccionario, se añade
        data[string] += 1 #si el string esta en el diccionario, se le suma 1
        if data[string] > valormax: #si el valor de la clave es mayor al valor maximo
            valormax = data[string]
            moda = string #se establece un nuevo valor maximo y una moda
    return moda