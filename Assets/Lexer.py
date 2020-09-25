# Tarea 3.2
# Jorge Arturo Méndez Vargas
# A01176369

# Primero importamos ply Lex para hacer el lexer
import ply.lex as lex

# Definimos las palabras reservadas
reserved = {
   'var' : 'VAR',
   'int' : 'INT',
   'program' : 'PROGRAM',
   'if' : 'IF',
   'else' : 'ELSE',
   'print' : 'PRINT',
   'float' : 'FLOAT'
}


# Definimos los tokens
tokens = ['ID', 'CTESTRING', 'INT', 'FLOAT', 'VAR', 'INT', 'PRINT', 'IF', 'ELSE', 'CTEI', 'CTEF', 'CTESTRING','SEMICOLON', 'SIMMAS', 'SIMMENOS',
 'SIMMULT', 'SIMDIV', 'COLON', 'BRACKETIZQ', 'BRACKETDER', 'PARENIZQ', 'PARENDER', 'PROGRAM', 'COMMA', 'MASQUE', 'MENOSQUE', 'IGUAL', 'NOIGUAL']

# Definimos las expresiones regulares para los tokens
t_ignore = ' \t'
t_CTESTRING = r'\".*\"'
t_SEMICOLON = r'\;'
t_SIMMAS = r'\+'
t_SIMMENOS = r'-'
t_SIMMULT = r'\*'
t_SIMDIV = r'\/'
t_COLON = r':'
t_BRACKETIZQ = r'\{'
t_BRACKETDER = r'\}'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_COMMA = r'\,'
t_MASQUE = r'>'
t_MENOSQUE = r'<'
t_IGUAL = r'\='
t_NOIGUAL = r'<>'
          
# También un error por si hay caracteres illegales
def t_error(t):
    print("caractér illegal '%s'" % t.value[0])
    t.lexer.skip(1)

#Definimos las expresiones regulares y acciones para los tokens que lo requieran
# ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# FLOAT
def t_CTEF(t):
    r'[0-9]*\.[0-9]+|[0-9]+'
    t.value = float(t.value)
    return t

# INT
def t_CTEI(t):
    r'\[0-9]+'
    t.value = int(t.value)
    return t

# COnstruimos el lexer
lexer = lex.lex()