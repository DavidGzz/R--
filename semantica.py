
variablesLocales = {}
variablesGlobales = {}
Funciones = {}

def add_variablesGlobales(id, tipo):
    variablesGlobales[id] = {
        'tipo': tipo,
    }

def add_variablesLocales(id, tipo):
    variablesLocales[id] = {
        'tipo' : tipo,
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
        return [variablesLocales[id]['tipo']]
    elif id in variablesGlobales:
        return [variablesGlobales[id]['tipo']]
    else :
        print("VARIABLE NO DECLARADA")
        exit(1)

def get_cuadruploFuncion(funcion):
    return Funciones[funcion]['cuadruplo']

def validar_Parametros(funcion, arreglo):
    if len(Funciones[funcion]['parametros']) != len(arreglo):
        return False
    arreglo.reverse()
    for x in Funciones[funcion]['parametros']:
        y1 = arreglo.pop()[1]
        y2 = x[1]
        if(y1 != y2) :
            return False
    return True

def get_VariablesFuncion(funcion):
    return len(Funciones[funcion]['variablesLocales'])