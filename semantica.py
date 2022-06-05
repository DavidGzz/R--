import memoria
variablesLocales = {}
variablesGlobales = {}
Funciones = {}

def add_variablesGlobales(memoria, id, tipo):
    dirMemoria = memoria.add_tipo(tipo)
    variablesGlobales[id] = {
        'tipo': tipo,
        'dirMemoria': dirMemoria,
    }

def add_variablesLocales(memoria, id, tipo):
    dirMemoria = memoria.add_tipo(tipo)
    variablesLocales[id] = {
        'tipo' : tipo,
        'dirMemoria': dirMemoria,
    }

def add_Funciones(id, tipo, parametros, cuadruplo):
    Funciones[id] = {
        'tipo' : tipo,
        'parametros' : parametros,
        'variablesLocales' : variablesLocales,
        'cuadruplo' : cuadruplo
    }

def get_tipoRetornoFuncion(funcionActual):
    return Funciones[funcionActual]['tipo']

def delete_VariablesLocales():
    global variablesLocales
    variablesLocales = {}

def delete_VariablesGlobales():
    variablesGlobales = {}

def existe_Global(id):
        if id in variablesGlobales:
            return True
        else:
            return False

def existe_Local(id):
    if id in variablesLocales:
        return True
    else:
        return False

def existe_Funcion(id):
    if id in Funciones:
        return True
    else:
        return False

def get_variable(id):
    if id in variablesLocales:
        return [variablesLocales[id]['dirMemoria'], variablesLocales[id]['tipo']]
    elif id in variablesGlobales:
        return [variablesGlobales[id]['dirMemoria'], variablesGlobales[id]['tipo']]
    else :
        print("VARIABLE NO DECLARADA")
        exit(1)

def get_cuadruploFuncion(funcion):
    return Funciones[funcion]['cuadruplo']

def validar_Parametros(funcion, arreglo):
    # revisa que sean la misma cantidad
    if len(Funciones[funcion]['parametros']) != len(arreglo):
        return False
    # Reverse al arreglo porque viene al reves
    arreglo.reverse()
    for x in Funciones[funcion]['parametros']:
        # Saca los tipos del parametro y de lo que se le manda
        y1 = arreglo.pop()[1]
        y2 = x[1]
        if(y1 != y2):
            return False
    return True

def get_VariablesFuncion(funcion):
    return len(Funciones[funcion]['variablesLocales'])