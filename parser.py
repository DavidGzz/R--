import ply.yacc as yacc
from semantica import delete_VariablesLocales, variablesLocales, variablesGlobales, add_variablesGlobales, add_variablesLocales, existe_Global, existe_Local, existe_Funcion, Funciones, add_Funciones
from lexer import tokens

scope = 1
popper = []
tipoActual = []
tipoRetorno = []
pilaOperadores = []
parametros = []
funcionActual = ""

def p_programa(p):
    '''programa : ID ';' vars programaF main'''

def p_main(p):
    '''main : MAIN '(' ')' bloque'''

def p_programaF(p):
    '''programaF : function programaF
                    | empty'''

def p_function(p):
    '''function : FUNCTION tipoRetorno ID '(' functionParam ')' functionAux bloque
                | empty'''

def p_functionAux(p):
    '''functionAux : '''
    global parametros
    global tipoRetorno
    global funcionActual
    if existe_Funcion(p[-4]):
        print("Error, funcion repetida")
        exit(1)
    else:
        funcionActual = p[-4]
        tipo = tipoRetorno.pop()
        add_Funciones(p[-4], tipo, parametros)
        parametros = []

def p_tipoRetorno(p):
    '''tipoRetorno : INT
                    | FLOAT
                    | VOID'''
    global tipoRetorno
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
                    | empty'''
                    #| for

def p_return(p):
    '''return : RETURN superexpresion ';' '''

def p_condicion(p):
    '''condicion : IF '(' superexpresion ')' bloque condicionelse'''

def p_condicionelse(p):
    '''condicionelse : ELSE bloque
                        | empty'''

def p_write(p):
    '''write : WRITE '(' superexpresion ')' ';' '''

#def p_for(p):
#    '''for : FOR '(' id oper superexpresion ';' asignacion ')' bloque'''

#def p_oper(p):
#    '''oper : '<'
#            | '>'
#            | EQUALS
#            | DIFF
#            | LTHANEQ
#            | GTHANEQ'''

def p_while(p):
    '''while : WHILE '(' superexpresion ')' bloque'''

def p_asignacion(p):
    '''asignacion : vars
                    | id asignacionp'''

def p_asignacionp(p):
    '''asignacionp : '=' superexpresion ';'
                    | '[' superexpresion ']' ';' '''

def p_superexpresion(p):
    '''superexpresion : megaexpresion superexpresionp'''

def p_superexpresionp(p):
    '''superexpresionp : AND superexpresion
                        | OR superexpresion
                        | empty'''

def p_megaexpresion(p):
    '''megaexpresion : exp megaexpresionp'''

def p_megaexpresionp(p):
    '''megaexpresionp : '<' exp
                        | '>' exp
                        | EQUALS exp
                        | DIFF exp
                        | LTHANEQ exp
                        | GTHANEQ exp
                        | empty'''

def p_exp(p):
    '''exp : termino expp'''

def p_expp(p):
    '''expp : '+' exp
            | '-' exp
            | empty'''

def p_termino(p):
    '''termino : factor terminop'''

def p_terminop(p):
    '''terminop : '*' exp
                | '/' exp
                | empty'''

def p_factor(p):
    '''factor : constante
                | '(' superexpresion ')' '''

def p_constante(p):
    '''constante : id
                | CTEF
                | CTEI'''

def p_functionParam(p):
    '''functionParam : parametro
                    | empty'''

def p_parametro(p):
    '''parametro : tipo ID parametrop'''
    global tipoActual
    tipo = tipoActual.pop()
    parametros.append([p[2],tipo])
    add_variablesLocales(p[2], tipo)

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
    global tipoActual
    tipo = tipoActual.pop()
    tipoActual.append(tipo)
    if scope == 1:
        if existe_Global(p[1]):
            print("Variable ya declarada")
            exit(1)
        else:
            add_variablesGlobales(p[1],tipo)
    else:
        if existe_Local(p[1]):
            print("Variable ya declarada")
            exit(1)
        else:
            add_variablesLocales(p[1], tipo)

def p_varsppp(p):
    '''varsppp : ',' varspp
                | empty'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR'''
    global tipoActual
    tipoActual.append(p[1])

def p_id(p): 
    '''id : ID idp'''

def p_idp(p): 
    '''idp : '[' superexpresion ']'
            | empty'''

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print("Syntax error in input!")
    print(p)

parser = yacc.yacc()

f = open("Prueba.txt", "r")

while True:
    try:
        s = f.read()
    except EOFError:
        break
    if not s: break
    parser.parse(s)

print("Variables Globales", variablesGlobales)
print("Variables Locales", variablesLocales)
print("Directorio de Funciones", Funciones)

f.close()