import ply.lex as lex

# Debe ignorar los espacios en blanco, tabulaciones, saltos de linea,  y comentarios
t_ignore = ' \t'

# Palabras reservadas (ver si me faltaron algunas)
reserved = {
    'skip' : 'TkSkip',
    'if'   : 'TkIf',
    'fi'   : 'TkFi',
    'do'   : 'TkDo',
    'od'   : 'TkOd',
    'for'  : 'TkFor',
    'rof'  : 'TkRof',
    'int'  : 'TkInt',
    'true' : 'TkTrue',
    'false': 'TkFalse',
    'print': 'TkPrint',
    'declare': 'TkDeclare',
    'array': 'TkArray',
    'bool' : 'TkBool',
}

tokens = [
    'TkSoForth', 'TkComma', 'TkOpenPar',
    'TkClosePar', 'TkAsig', 'TkSemicolon', 'TkArrow', 'TkPlus',
    'TkMinus', 'TkMult', 'TkNot', 'TkLess',
    'TkLeq', 'TkGeg', 'TkGreater', 'TkEqual', 'TkNEqual',
    'Tk0Bracket', 'TkCBracket', 'TkTwoPoints', 'TkConcat',
    'TkId', 'TkNum', 'TkString', 'TkAnd', 'TkOr',
    'Tk0Block', 'TkCBlock'
]

t_TkPlus = r'\+'
t_TkOpenPar = r'\('
t_TkClosePar = r'\)'
t_TkNot = r'\!'
t_Tk0Bracket = r'\['
t_TkCBracket = r'\]'
t_TkMult = r'\*'
t_Tk0Block = r'\|\['
t_TkCBlock = r'\]\|'
t_TkAnd = r'/\\'
t_TkOr = r'\\/'
t_TkSoForth = r'\.\.'
t_TkConcat = r'\.'
t_TkComma = r','
t_TkAsig = r':='
t_TkSemicolon = r';'
t_TkArrow = r'-->'
t_TkMinus = r'-'
t_TkLess = r'<'
t_TkLeq = r'<='
t_TkGeg = r'>='
t_TkGreater = r'>'
t_TkEqual = r'='
t_TkNEqual = r'!='
t_TkTwoPoints = r':'

tokens = tokens + list(reserved.values())

def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'TkId')    # Check for reserved words
    return t

def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TkString(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remueve las comillas
    return t

# Ignora nuevas lineas
def t_newline(t):
    r'\n+'
    pass

# Ignora comentarios
def t_comment(t):
    r'//.*'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
|[
declare
a, b, c : int;
d, e, f : array[0..2]
a := b + 3;
print e
// Esto es un comentario. Debe ser ignorado.
]|
'''

# Give the lexer some input
lexer.input(data)
 
# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break
    else:
        if tok.type == 'TkId':
            print(tok.type + "(\"" + tok.value + "\")", tok.lineno, tok.lexpos)
        elif tok.type == 'TkNum':
            print(tok.type + "(" + str(tok.value) + ")", tok.lineno, tok.lexpos)
        elif tok.type == 'TkString':
            print(tok.type + "(\"" + tok.value + "\")", tok.lineno, tok.lexpos)
        else:
            print(tok.type, tok.lineno, tok.lexpos)

### Cosas que faltan: ###
# - Detectar errores
# - Ver si hay más palabras reservadas
# - Crear función main donde se pida el input que va a pasar a través del lexer
# - Imprimir fila y columna correctamente