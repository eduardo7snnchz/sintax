import ply.lex as lex
 
    #Definición de tokens que identificara/reconocera el analizador 
tokens = ['SUMA','RESTA','MULTIPLICACION','DIVISION','POTENCIA','RESTO', 'NUMERO',                                          
            'MENORQUE', 'MAYORQUE', 'IGUAL', 'DIFERENTE', 'MENOROIGUALQUE','MAYOROIGUALQUE',               
            'AND', 'OR',
            'IF', 'ELSE', 'SWITCH', 'WHILE','FOR', 'DO','CASE',
            'PARENTESISI', 'PARENTESISD',
                                                                                          
]

t_PARENTESISI = r'\('
t_PARENTESISD = r'\)'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_POTENCIA = r'\*\*'
t_RESTO = r'\%'
t_MENORQUE = r'\<'
t_MAYORQUE = r'\>'
t_IGUAL = r'\=\='
t_DIFERENTE = r'\!\='
t_MENOROIGUALQUE = r'\<\='
t_MAYOROIGUALQUE = r'\>\='
t_AND = r'and'
t_OR = r'or'
t_IF = r'if'
t_ELSE = r'else'
t_SWITCH = r'switch'
t_WHILE = r'while'
t_FOR = r'for'
t_DO = r'do'
t_CASE = r'case'



    # Para identificar que sea número entero
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

    # Para saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    # Ignorar tabs y espacios
t_ignore  = ' \t'

    # Para el manejo de errores (caracteres no admitidos)
def t_error(t):
    print("Caracter no admitido '%s'" % t.value[0])
    t.lexer.skip(1)

    # Construye el analizador léxico
lexer = lex.lex()

    # Input para verificar cadenas
lexer.input(input())

    # Manejo de tokens
while True:
    tok = lexer.token()
    if not tok:
        break     
    print(tok)
