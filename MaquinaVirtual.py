import json
import math
from memoria import Memoria

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
auxVar = ""
isRead = 0

# Función que regresa el valor dado una dirección de memoria
def get_Valor(c):
    try:
        if isinstance(c, list):
            c = get_Valor(c[0])
        #if isRead == 1:
        #    isRead = 0
        #    return temporal[c]
        if c in variablesGlobales:
            return variablesGlobales[c]
        if c < 400:
            return variablesLocales[c]
        elif c < 800:
            return variablesGlobales[c]
        elif c < 1200:
            return constantes[c]
        elif c < 1600:
            return temporal[c]
        else:
            return variablesGlobales[c]
    except:
        print("Variable no tiene valor")
        print(c)
        exit(1)

def suma(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) + float(get_Valor(c2))
    except:
        exit(1)

def resta(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) - float(get_Valor(c2))
    except:
        exit(1)

def multiplicacion(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) * float(get_Valor(c2))
    except:
        exit(1)

def division(c1, c2, c3):
    try:
        temporal[c3] = float(get_Valor(c1)) / float(get_Valor(c2))
    except:
        exit(1)

def goto(c1, c2, c3):
	global cont
	cont = c3 - 1

def gotoF(c1, c2, c3):
	global cont
	if not temporal[c1]:
		cont = c3 - 1

def asignacion(c1, c2, c3):
    # Checa el valor de c3 que es la variable a asignar
    global temporal
    if isinstance(c3, list):
        c3 = get_Valor(c3[0])
    if c3 < 400:
        global variablesLocales
        variablesLocales[c3] = get_Valor(c1)
    elif c3 < 800:
        variablesGlobales[c3] = get_Valor(c1)
    elif c3 < 1200:
        global constantes
        constantes[c3] = get_Valor(c1)
    else:
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

def read(c1, c2, c3):
    global cont
    global isRead
    c2 = float(input())
    temporal[c3] = c2
    #cuadruplos[cont][0] = '='
    #cuadruplos[cont][1] = int(c2)
    #cuadruplos[cont][3] = temporal[c3]
    #print("K:", cuadruplos[cont])
    #cont = cont - 1
    isRead = 1

def era(c1, c2, c3):
    global stackMemoria
    global variablesLocales
    #print("VariablesLoc:", variablesLocales)
    #print("Temporal:", temporal)
    #print("Cont:", cont)
    stackMemoria.append([cont, variablesLocales, temporal])
    #print("StackMEMORIA ERA:", stackMemoria)
    #print("StackMEMORIA ERA[1]:", stackMemoria[-1])
    global parametros
    parametros = todo['funciones'][c2]
    #print("PARAMETROS:", parametros)

def retorno(c1, c2, c3):
    variablesGlobales[c1] = get_Valor(c3)

def gosub(c1, c2, c3):
    global cont
    global variablesLocales
    global auxLocales
    #print("Stack Memoria GOSUB", stackMemoria)
    aux = stackMemoria.pop()
    #print("AUX:", aux)
    aux[0] = cont
    stackMemoria.append(aux)
    cont = c1 - 1
    #print("AUXLOCALES:", auxLocales)
    variablesLocales = auxLocales

def parametro(c1, c2, c3):
    global auxLocales
    x = list(reversed(parametros['parametros']))[c3 - 1]
    auxLocales[parametros['variablesLocales'][x[0]]['dirMemoria']] = get_Valor(c1)
    
def endfunc(c1, c2, c3):
    global variablesLocales
    global temporal
    global cont
    #print("Stack Memoria END", stackMemoria)
    funcion = stackMemoria.pop()
    #print("Funcion:", funcion)
    #print("Funcion0:", funcion[0])
    #print("Funcion1:", funcion[1])
    #print("Funcion2:", funcion[2])
    cont = funcion[0]
    variablesLocales = funcion[1]
    temporal = funcion[2]

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

# Todas las operaciones que puede tener el programa
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
    'writeL': writeL,
    'era' : era,
    'return' : retorno,
    'gosub' : gosub,
    'param' : parametro,
    'ENDFUNC' : endfunc,
    '==' : igualIgual,
    'read' : read,
    'fact' : fact,
    'cuadratica' : cuadratica,
    'fib' : fibonacci,
    'raiz' : raiz,

}

# Abre el archivo y lo mete en una variable
with open("cuadruplos.json") as f:
    todo = json.load(f)

# Mete las constantes en una variable
constantes = todo['constantes']
# Las constantes vienen al reves, asi es que se le hace reverse
constantes = {v: k for k, v in constantes.items()}
# Mete los cuadruplos a una variable
cuadruplos = todo['cuadruplos']

# While que pasa por cada cuadruplo
while cont < len(cuadruplos):
    cuad = cuadruplos[cont]
    operaciones[cuad[0]](cuad[1], cuad[2], cuad[3])
    cont = cont + 1