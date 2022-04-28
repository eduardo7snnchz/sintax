import ply.yacc as yacc

# Para importar los tokens del analizador léxico
from lexico import tokens

def p_expression_plus(p):
    'expression : expression AND term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression RESTA term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term MULTIPLICACION factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVISION factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : PARENTESISI expression PARENTESISD'
    p[0] = p[2]

def p_term_potencia(p):
    'term : term POTENCIA term'
    p[0] = p[1]*p[1]

def p_term_modulo(p):
    'term : term RESTO term'
    p[0] = p[1]/p[1]

def p_expression_mayor(p):
    'expression : term MAYORQUE term'
    p[0] = p[1] > p[3]

def p_expression_menor(p):
    'expression : term MENORQUE term'
    p[0] = p[1] < p[3]

def p_expression_igual(p):
    'expression : term IGUAL term'
    p[0] = p[1] == p[3]

def p_expression_mayorq(p):
    'expression : term MAYOROIGUALQUE term'
    p[0] = p[1] >= p[3]

def p_expression_menorq(p):
    'expression : term MENOROIGUALQUE term'
    p[0] = p[1] <= p[3]

def p_expression_dif(p):
    'expression : term DIFERENTE term'
    p[0] = p[1] != p[3]

#def p_expression_and(p):
 #   'expression : term AND term'
  #  p[0] = p[1] and p[3]




# Para el manejo de erroes en el input 
def p_error(p):
    print("Syntax error!")

# Para construir el parser
parser = yacc.yacc()

while True:
   try:
       s = input('INPUT: ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
