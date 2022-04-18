
variablesLocales = {}
variablesGlobales = {}
Funciones = {}

def add_variablesGlobales(id, tipo):
    variablesGlobales[id] = {
        'tipo': tipo,
    }

def add_variablesLocales(id, tipo):
    variablesLocales[id] = {
        'tipo': tipo,
    }

def add_Funciones(id, tipo, parametros):
    #global variablesLocales
    Funciones[id] = {
        'tipo' : tipo,
        'parametros' : parametros
        #'VariablesLocales' : variablesLocales
    }

def delete_VariablesLocales():
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