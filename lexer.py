import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'return' : 'RETURN',
    'function' : 'FUNCTION',
    'int' : 'INT',
    'float' : 'FLOAT',
    'void' : 'VOID',
    'char' : 'CHAR',
    'write' : 'WRITE',
    'main' : 'MAIN',
}

tokens = [
    'ID',
    'GTHANEQ',
    'LTHANEQ',
    'EQUALS',
    'OR',
    'AND',
    'DIFF',
    'CTEI',
    'CTEF',
    'LETRERO',
] + list(reserved.values())

literals = ";:,{}[]()<>=|&+-*/"

t_ignore = ' \t'
t_CTEI = r'[0-9]+'
t_CTEF = r'[0-9]+\.[0-9]+'
t_LETRERO = r'".*"'
t_DIFF = r'<>'
t_GTHANEQ = r'>='
t_LTHANEQ = r'<='
t_EQUALS = r'=='
t_OR = r'\|\|'
t_AND = r'&&'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print("token ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

f = open("Prueba7.txt", "r")
data = f.read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok: 
        break     
    #print(tok)