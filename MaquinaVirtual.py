import json
import math

from semantica import get_variable

constantes = {}
variablesGlobales = {}
variablesLocales = {}
temporal = {}
stackMemoria = []
parametros = []
auxLocales = {}
cont = 0
contAux = 0
contAux1 = 0
contAux2 = 1

def get_Valor(c):
    try:
        if c in variablesGlobales:
            return variablesGlobales[c]
        if c / 400.0 < 1:
            return variablesLocales[c]
        elif c / 800.0 < 1:
            return variablesGlobales[c]
        elif c / 1200.0 < 1:
            return constantes[c]
        elif c / 1600.0 < 1:
            return temporal[c]
        else:
            return variablesGlobales[c]
    except:
        print("Variable no tiene valor")
        print(c)

def suma(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) + float(get_Valor(c2))
    except:
        exit(-1)

def resta(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) - float(get_Valor(c2))
    except:
        exit(-1)

def multiplicacion(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) * float(get_Valor(c2))
    except:
        exit(-1)

def division(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) / float(get_Valor(c2))
    except:
        exit(-1)

def goto(c1, c2, c3):
	global cont
	cont = c3 - 1

def gotoF(c1, c2, c3):
	global cont
	if not temporal[c1]:
		cont = c3 - 1

def asignacion(c1, c2, c3):
    if c3 / 400 < 1:
        global variablesLocales
        variablesLocales[c3] = get_Valor(c1)
    elif c3 / 800 < 1:
        variablesGlobales[c3] = get_Valor(c1)
    elif c3 / 1200 < 1:
        global constantes
        constantes[c3] = get_Valor(c1)
    else:
        global temporal
        temporal[c3] = get_Valor(c1)

def mayorQ(c1, c2, c3):
	if float(get_Valor(c1)) > float(get_Valor(c2)):
		temporal[c3] = True
	else: 
		temporal[c3] = False

def menorQ(c1, c2, c3):
	global temporal
	if float(get_Valor(c1)) < float(get_Valor(c2)):
		temporal[c3] = True
	else: 
		temporal[c3] = False

def write(c1, c2, c3):
    print(get_Valor(c3))

def era(c1, c2, c3):
	global stackMemoria
	global variablesLocales
	stackMemoria.append([cont, variablesLocales, temporal])
	global parametros
	parametros = todo['funciones'][c2]

def retorno(c1, c2, c3):
    global variablesGlobales
    global cont
    variablesGlobales[c1] = get_Valor(c3)
    cont = contAux1

def ret(c1, c2, c3):
    global cont
    cont = contAux1 + 1

def gosub(c1, c2, c3):
    global cont
    global contAux
    global contAux1
    global contAux2
    if contAux2 == 1:
        contAux1 = cont
        contAux2 = 0
    contAux = cont
    cont = c1 - 1
    global variablesLocales
    variablesLocales = auxLocales 

def parametro(c1, c2, c3):
    global auxLocales
    x = list(reversed(parametros['parametros']))[c3 - 1]
    auxLocales[parametros['variablesLocales'][x[0]]['dirMemoria']] = get_Valor(c1)
    
def endfunc(c1, c2, c3):
    global cont
    cont = contAux

def igualIgual(c1, c2, c3):
    global temporal
    if float(get_Valor(c1)) == float(get_Valor(c2)):
        temporal[c3] = True
    else:
        temporal[c3] = False

def menorOIGUAL(c1, c2, c3):
    global temporal
    if float(get_Valor(c1)) <= float(get_Valor(c2)):
        temporal[c3] = True
    else:
        temporal[c3] = False

def mayorOIGUAL(c1, c2, c3):
    global temporal
    if float(get_Valor(c1)) >= float(get_Valor(c2)):
        temporal[c3] = True
    else:
        temporal[c3] = False

def writeL(c1, c2, c3):
    print(c3)

def fact(c1, c2, c3):
    num = int(c1)
    respuesta = math.factorial(num)
    print("Factorial de", c1, "=", respuesta)


def cuadratica(c1, c2, c3):
    a = int(c1)
    b = int(c2)
    c = int(c3)
    respuesta = (-b + (math.sqrt(math.pow(b, 2) - (4 * a * c)))) / (2 * a)
    respuesta1 = (-b - (math.sqrt(math.pow(b, 2) - (4 * a * c)))) / (2 * a)
    print("Resultado 1 =", respuesta)
    print("Resultado 2 =", respuesta1)

def fibonacci(c1, c2, c3):
    num = int(c1)
    aux = 0
    aux1 = 1
    sig = 0
    x = 1
    while(x <= num):
        if x == 1:
            print(aux)
        if x == 2:
            print(aux1)
        sig = aux + aux1
        aux = aux1
        aux1 = sig
        print(sig)
        x = x + 1

def raiz(c1, c2, c3):
    num = int(c1)
    respuesta = math.sqrt(num)
    print("Raiz cuadrada de", num, "=", respuesta)


operaciones = {
    '+': suma,
    'goto': goto,
    'gotoF': gotoF,
    '=': asignacion,
    '-': resta,
    '/': division,
    '*': multiplicacion,
    '>': mayorQ,
    '<': menorQ,
    '<=': menorOIGUAL,
    '>=': mayorOIGUAL,
    'write': write,
    'era' : era,
    'return' : retorno,
    'gosub' : gosub,
    'param' : parametro,
    'ENDFUNC' : endfunc,
    '==' : igualIgual,
    'ret' : ret,
    'fact' : fact,
    'cuadratica' : cuadratica,
    'fib' : fibonacci,
    'raiz' : raiz,

}

with open('cuadruplos.json') as f:
    todo = json.load(f)

constantes = todo['constantes']
constantes = {v: k for k, v in constantes.items()}
cuadruplos = todo['cuadruplos']
#llenarVariablesLocales('main')
cuad1 = cuadruplos[cont]

while cont < len(cuadruplos):
	cuad = cuadruplos[cont]
	operaciones[cuad[0]](cuad[1], cuad[2], cuad[3])
	cont = cont + 1