from asyncio.windows_events import NULL
import ply.yacc as yacc
from semantica import delete_VariablesLocales, variablesLocales, variablesGlobales, add_variablesGlobales, get_variable
from semantica import add_variablesLocales, existe_Global, existe_Local, existe_Funcion, Funciones, add_Funciones
from semantica import get_tipoRetornoFuncion, get_cuadruploFuncion, validar_Parametros, get_VariablesFuncion
from lexer import tokens
from CuboSemantico import cuboSemantico
from memoria import Memoria
import json

scope = 1
tipoWrite = 0
totalParametros = 0
temporal = []
temporal1 = []
pOper = []
pilaO = []
cuadruplo = []
tipoActual = []
tipoRetorno = []
parametros = []
pilaSaltos = []
stackFor = []
constantes = {}
cuadruploFuncion = 0
funcionActual = ""
writeActual = ""
mLocal = Memoria(0, 100, 200, 300, 400)
mGlobal = Memoria(400, 500, 600, 700, 800)
mConsts = Memoria(800, 900, 1000, 1100, 1200)
mTemp = Memoria(1200, 1300, 1400, 1500, 1600)
retorna = None

def p_programa(p):
    '''programa : ID primerCuad ';' vars programaF main'''

def p_primerCuad(p):
    '''primerCuad : '''
    cuadruplo.append(['goto', '0', '0', '0'])

def p_main(p):
    '''main : MAIN llenarCuad '(' ')' bloque'''

def p_llenarCuad(p):
    '''llenarCuad : '''
    cuadruplo[0] = ['goto', '0', '0', len(cuadruplo)]

def p_programaF(p):
    '''programaF : function programaF
                    | empty'''

def p_function(p):
    '''function : FUNCTION tipoRetorno ID '(' functionParam ')' functionAux bloque functionAux2
                | empty'''

def p_functionAux(p):
    '''functionAux : '''
    global parametros
    global cuadruploFuncion
    cuadruploFuncion = len(cuadruplo)
    if existe_Funcion(p[-4]):
        print("ERROR, funcion repetida")
        exit(1)
    else:
        global funcionActual
        funcionActual = p[-4]
        tipo = tipoRetorno.pop()
        add_Funciones(p[-4], tipo, parametros, cuadruploFuncion)
        parametros = []

def p_functionAux2(p):
    '''functionAux2 : '''
    tipo = get_tipoRetornoFuncion(funcionActual)
    if not retorna and tipo != 'void':
        print('LA FUNCION DEBE RETORNAR ALGO')
        exit(1)
    if tipo == 'void':
        cuadruplo.append(['ret', '0', '0', '0'])
    if retorna:
        if(retorna[1] != tipo) and tipo != 'void':
            print("Type Mistmatch")
            exit(1)

    cuadruplo.append(['ENDFUNC', '0', '0', '0'])
    global mLocal
    mLocal = Memoria(0, 100, 200, 300,400)
    global mTemp
    mTemp = Memoria(1200, 1300, 1400, 1500, 1600)
    delete_VariablesLocales()

def p_tipoRetorno(p):
    '''tipoRetorno : INT
                    | FLOAT
                    | VOID'''
    tipoRetorno.append(p[1])

def p_bloque(p):
    '''bloque : '{' cuerpo '}' '''

def p_cuerpo(p):
    '''cuerpo : vars estatutop'''

def p_estatutop(p):
    '''estatutop : estatuto estatutop
                    | empty'''

def p_estatuto(p):
    '''estatuto : asignacion
                    | condicion
                    | write
                    | while
                    | return
                    | for
                    | id ';'
                    | empty'''

def p_return(p):
    '''return : RETURN superexpresion ';' '''
    global retorna
    retorna = pilaO.pop()
    tipo = get_tipoRetornoFuncion(funcionActual)
    if retorna and tipo != 'void' and retorna[1] == tipo:
        cuadruplo.append(['return', funcionActual, '0', retorna[0]])
        #cuadruplo.append(['ret', '0', '0', '0'])
    elif tipo != 'void' and tipo != retorna[1]:
        print('TIPO DE RETORNO EQUIVOCADO')
        exit(-1)
    elif retorna and tipo == 'void':
        print('FUNCIONES VOID NO PUEDEN RETORNAR ALGO')
        exit(1)

def p_condicion(p):
    '''condicion : IF '(' superexpresion ')' condicionAux bloque condicionelse'''

def p_condicionAux(p):
    '''condicionAux : '''
    cond = pilaO.pop()
    if cond[1] != 'bool':
        print('TYPE_MISMATCH')
        exit(1)
    else:
        pilaSaltos.append(len(cuadruplo))
        cuadruplo.append(['gotoF', cond[0], '0', '0'])

def p_condicionelse(p):
    '''condicionelse : ELSE condicionelseAux bloque
                        | empty'''
    salida = pilaSaltos.pop()
    cuadruplo[salida] = [cuadruplo[salida][0], cuadruplo[salida][1], '0', len(cuadruplo)]

def p_condicionelseAux(p): 
    '''condicionelseAux : '''
    salida = pilaSaltos.pop()
    cuadruplo[salida] = [cuadruplo[salida][0], cuadruplo[salida][1], '0', len(cuadruplo) + 1]
    pilaSaltos.append(len(cuadruplo))
    cuadruplo.append(['goto', '0', '0', '0'])

def p_write(p):
    '''write : WRITE '(' writep ')' ';' '''

def p_writep(p): 
    '''writep : superexpresion writepAux writepp
              | LETRERO writepAux2 writepp''' 

def p_writepAux(p): 
    '''writepAux : ''' 
    global tipoWrite
    tipoWrite = 1

def p_writepAux2(p): 
    '''writepAux2 : '''
    global tipoWrite
    global writeActual
    tipoWrite = 2
    writeActual = p[-1]

def p_writepp(p): 
    '''writepp : ',' writeppAux writep
                | empty writeppAux'''

def p_writeppAux(p): 
    '''writeppAux : ''' 
    if tipoWrite == 1:
        varWrite = pilaO.pop()
        cuadruplo.append(['write', '0', '0', varWrite[0]])
    elif tipoWrite == 2:
        cuadruplo.append(['write', '0', '0', writeActual])

def p_for(p):
    '''for : FOR '(' id '=' superexpresion forAux ';' superexpresion forAux2 ')' bloque forAux3'''

def p_forAux(p):
    '''forAux : '''
    valor = pilaO.pop()
    idd = pilaO.pop()
    cuadruplo.append(['=', valor[0], '0', idd[0]])

def p_forAux2(p):
    '''forAux2 : '''
    condicion = pilaO.pop()
    pilaSaltos.append(len(cuadruplo))
    cuadruplo.append(['gotoF', condicion[0], '0', '0'])

def p_forAux3(p):
    '''forAux3 : '''
    salida = pilaSaltos.pop()
    cuadruplo[salida] = [cuadruplo[salida][0], cuadruplo[salida][1], '0', len(cuadruplo) + 1]
    cuadruplo.append(['goto', '0', '0', salida - 1])

def p_while(p):
    '''while : WHILE whileAux '(' superexpresion ')' whileAux2 bloque'''
    falso = pilaSaltos.pop()
    retorno = pilaSaltos.pop()
    cuadruplo.append(['goto', '0', '0', retorno])
    cuadruplo[falso] = [cuadruplo[falso][0], cuadruplo[falso][1], '0', len(cuadruplo)]

def p_whileAux(p):
    '''whileAux : '''
    pilaSaltos.append(len(cuadruplo))

def p_whileAux2(p):
    '''whileAux2 : '''
    cond = pilaO.pop()
    if cond[1] != 'bool':
        print("TYPE MISTMATCH")
    else:
        pilaSaltos.append(len(cuadruplo))
        cuadruplo.append(['gotoF', cond[0], '0', '0'])

def p_asignacion(p):
    '''asignacion : vars
                    | id asignacionp'''

def p_asignacionp(p):
    '''asignacionp : '=' superexpresion ';' '''
    asignar = pilaO.pop()
    asignarA = pilaO.pop()
    cuadruplo.append(['=',  asignar[0], '0', asignarA[0]])

def p_superexpresion(p):
    '''superexpresion : megaexpresion superexpresionp'''
    if pOper: 
        if pOper[-1] == '&&' or pOper[-1] == '||':
            operador = pOper.pop()
            op1 = pilaO.pop()
            op2 = pilaO.pop()
            tipo = cuboSemantico.get((op2[1], operador, op1[1]), 'error')
            if tipo != 'error' :
                respuesta = mTemp.add_tipo(tipo)
                cuadruplo.append([operador, op2[0], op1[0], respuesta])
                pilaO.append([respuesta, tipo])
            else:
                print("ERROR TYPE MISTMATCH *")
                exit(1)


def p_superexpresionp(p):
    '''superexpresionp : AND superexpresion
                        | OR superexpresion
                        | empty'''
    if p[1]:
        pOper.append(p[1])

def p_megaexpresion(p):
    '''megaexpresion : exp megaexpresionp'''
    if pOper: 
        if pOper[-1] == '<' or pOper[-1] == '>' or pOper[-1] == '>=' or pOper[-1] == '<=' or pOper[-1] == '<>' or pOper[-1] == '==':
            operador = pOper.pop()
            op1 = pilaO.pop()
            op2 = pilaO.pop()
            tipo = cuboSemantico.get((op2[1], operador, op1[1]), 'error')
            if tipo != 'error' :
                respuesta = mTemp.add_tipo(tipo)
                cuadruplo.append([operador, op2[0], op1[0], respuesta])
                pilaO.append([respuesta, tipo])
            else:
                print("ERROR TYPE MISTMATCH *")
                exit(1)

def p_megaexpresionp(p):
    '''megaexpresionp : '<' exp
                        | '>' exp
                        | EQUALS exp
                        | DIFF exp
                        | LTHANEQ exp
                        | GTHANEQ exp
                        | empty'''
    if p[1]:
        pOper.append(p[1])

def p_exp(p):
    '''exp : termino expp'''
    #print("POPER+: ", pOper)
    if pOper: 
        if pOper[-1] == '+' or pOper[-1] == '-':
            global cuadruplo
            operador = pOper.pop()
            op1 = pilaO.pop()
            op2 = pilaO.pop()
            tipo = cuboSemantico.get((op2[1], operador, op1[1]), 'error')
            if tipo != 'error' :
                respuesta = mTemp.add_tipo(tipo)
                cuadruplo.append([operador, op2[0], op1[0], respuesta])
                pilaO.append([respuesta, tipo])
            else:
                print("ERROR TYPE MISTMATCH +")
                exit(1)

def p_expp(p):
    '''expp : '+' pAppT exp
            | '-' pAppT exp
            | empty'''
    #if p[1]:
    #    pOper.append(p[1])

def p_pAppT(p):
    '''pAppT : '''
    if pOper:
        if pOper[-1] == '*' or pOper[-1] == '/' or pOper[-1] == '+' or pOper[-1] == '-':
            global cuadruplo
            operador = pOper.pop()
            op1 = pilaO.pop()
            op2 = pilaO.pop()
            tipo = cuboSemantico.get((op2[1], operador, op1[1]), 'error')
            if tipo != 'error' :
                respuesta = mTemp.add_tipo(tipo)
                cuadruplo.append([operador, op2[0], op1[0], respuesta])
                pilaO.append([respuesta, tipo])
            else:
                print("ERROR TYPE MISTMATCH +")
                exit(1)
    pOper.append(p[-1])

def p_termino(p):
    '''termino : factor terminop'''
    #print("POPER*: ", pOper)
    if pOper:
        if pOper[-1] == '*' or pOper[-1] == '/':
            global cuadruplo
            operador = pOper.pop()
            op1 = pilaO.pop()
            op2 = pilaO.pop()
            tipo = cuboSemantico.get((op2[1], operador, op1[1]), 'error')
            if tipo != 'error':
                respuesta = mTemp.add_tipo(tipo)
                cuadruplo.append([operador, op2[0], op1[0], respuesta])
                pilaO.append([respuesta, tipo])
            else:
                print("ERROR TYPE MISTMATCH *")
                exit(1)

def p_terminop(p):
    '''terminop : '*' pAppF termino
                | '/' pAppF termino
                | empty'''
    #if p[1]:
    #    pOper.append(p[1])

def p_pAppF(p):
    '''pAppF : '''
    if pOper:
        if pOper[-1] == '+' or pOper[-1] == '-' or pOper[-1] == '':
            pOper.append(p[-1])
        elif pOper[-1] == '*' or pOper[-1] == '/':
            global cuadruplo
            operador = pOper.pop()
            op1 = pilaO.pop()
            op2 = pilaO.pop()
            tipo = cuboSemantico.get((op2[1], operador, op1[1]), 'error')
            if tipo != 'error':
                respuesta = mTemp.add_tipo(tipo)
                cuadruplo.append([operador, op2[0], op1[0], respuesta])
                pilaO.append([respuesta, tipo])
            else:
                print("ERROR TYPE MISTMATCH *")
                exit(1)
            pOper.append(p[-1])
    else:
        pOper.append(p[-1])
    

def p_factor(p):
    '''factor : constante
                | lParen superexpresion rParen '''

def p_lParen(p):
    '''lParen : '(' '''
    pOper.append(p[1])

def p_rParen(p):
    '''rParen : ')' '''
    pOper.pop()

def p_constante(p):
    '''constante : id
                | CTEF ctef
                | CTEI ctei'''

def p_ctef(p):
    '''ctef : '''
    if p[-1] not in constantes:
        constantes[p[-1]] = mConsts.add_tipo('float')
    pilaO.append([constantes[p[-1]], 'float'])

def p_ctei(p):
    '''ctei : '''
    if p[-1] not in constantes:
        constantes[p[-1]] = mConsts.add_tipo('int')
    pilaO.append([constantes[p[-1]], 'int'])

def p_functionParam(p):
    '''functionParam : parametro
                    | empty'''

def p_parametro(p):
    '''parametro : tipo ID parametrop'''
    tipo = tipoActual.pop()
    parametros.append([p[2], tipo])
    add_variablesLocales(mLocal, p[2], tipo)

def p_parametrop(p):
    '''parametrop : ',' parametro
                | empty'''

def p_vars(p):
    '''vars : varsp'''
    global scope
    scope = 2

def p_varsp(p):
    '''varsp : tipo varspp ';' varsp
                | empty'''

def p_varspp(p):
    '''varspp : ID varsppp'''
    tipo = tipoActual.pop()
    tipoActual.append(tipo)
    if scope == 1:
        if existe_Global(p[1]):
            print("Variable ya declarada")
            exit(1)
        else:
            add_variablesGlobales(mGlobal, p[1], tipo)
    else:
        if existe_Local(p[1]):
            print("Variable ya declarada")
            exit(1)
        elif existe_Global(p[1]):
            print("Variable ya declarada")
            exit(1)
        else:
            add_variablesLocales(mLocal, p[1], tipo)

def p_varsppp(p):
    '''varsppp : ',' varspp
                | '[' CTEI ']' arreglo
                | empty'''

def p_arreglo(p):
    '''arreglo : ',' varspp
                | empty'''
    

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR'''
    tipoActual.append(p[1])

def p_id(p): 
    '''id : ID idp'''

def p_idp(p): 
    '''idp : '(' idpp ')'
            | '[' superexpresion ']'
            | empty'''
    global totalParametros
    if p[1] == '(':
        if existe_Funcion(p[-1]):
            global temporal
            global temporal1
            for x in range(0, totalParametros):
                aux = pilaO.pop()
                temporal.append(aux)
                temporal1.append(aux)
            if validar_Parametros(p[-1], temporal):
                cuadruplo.append(['era', get_VariablesFuncion(p[-1]), p[-1], '0'])
                for x in temporal1:
                    cuadruplo.append(['param', x[0], '0', totalParametros])
                    totalParametros = totalParametros - 1
                temporal1 = []
                cuadruplo.append(['gosub', get_cuadruploFuncion(p[-1]), p[-1], '0'])
                if get_tipoRetornoFuncion(p[-1]) != 'void':
                    respuesta = mTemp.add_tipo(get_tipoRetornoFuncion(p[-1]))
                    cuadruplo.append(['=', p[-1], '0', respuesta])
                    pilaO.append([respuesta, get_tipoRetornoFuncion(p[-1])])
            else :
                print("ERROR, parametros equivocados")
                exit(1)
    else:
        variable = get_variable(p[-1])
        pilaO.append([variable[0], variable[1]])

def p_idpp(p):
    '''idpp : superexpresion idppp
            | empty'''

def p_idppp(p):
    '''idppp : ',' idpp
            | empty'''
    global totalParametros
    totalParametros = totalParametros + 1

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print("Syntax error in input!")
    print(p)

parser = yacc.yacc()

f = open("Prueba8.txt", "r")

while True:
    try:
        s = f.read()
    except EOFError:
        break
    if not s: break
    parser.parse(s)

#print("Variables Globales", variablesGlobales)
#print("Variables Locales", variablesLocales)
#print("Directorio de Funciones", Funciones)
#print("CONSTANTES", constantes)
cont = 0
print("Cuadruplos")
for x in cuadruplo:
    print(cont, ": ", cuadruplo[cont])
    cont = cont + 1

f.close()

diccionario = {
            'funciones': Funciones,
            'cuadruplos': cuadruplo ,
            'constantes': constantes,
            'globals': variablesGlobales,
    }

with open('cuadruplos.json', 'w') as f:
    json.dump(diccionario, f)