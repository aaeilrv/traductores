import ply.lex as lex

# Debe ignorar los espacios en blanco, tabulaciones, saltos de linea,  y comentarios
t_ignore = ' \t'

# Palabras reservadas
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
    'Tk0Block', 'TkCBlock', 'TkGuard',
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
t_TkEqual = r'=='
t_TkNEqual = r'!='
t_TkTwoPoints = r':'
t_TkGuard = r'\[\]'

tokens = tokens + list(reserved.values())

def t_TkId(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'TkId')    # Check for reserved words
    return t

def t_TkNum(t):
    r'\d+'
    t.value = int(t.value)
    return t

#hacer que reconozca \" como un caracter"
def t_TkString(t):
    r'\".*?"'
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

line_g = 0
error = []

# Error handling rule
def t_error(t):
    global error
    error.append('Error: Unexpected character {} in row {}, colum P{}'.format(t.value[0],line_g,t.lexpos+1))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Give the lexer some input
def work(data,line, correct):
    global error
    global line_g

    line_g = line
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
        else:
            if tok.type == 'TkId':
                correct.append('{}(\"{}\"), {}, {}'.format(tok.type, tok.value, line, tok.lexpos +1))
            elif tok.type == 'TkNum':
                correct.append('{}({}), {}, {}'.format(tok.type, tok.value, line, tok.lexpos +1))
            elif tok.type == 'TkString':
                correct.append('{}(\"{}\"), {}, {}'.format(tok.type, tok.value, line, tok.lexpos +1))
            else:
                correct.append('{}({}, {}, {})'.format(tok.type, line, tok.lexpos +1, tok.value))
    
    return error