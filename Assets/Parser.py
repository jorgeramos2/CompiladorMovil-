#Importamos ply yacc para el parser y los tokens del lexer.
import ply.yacc as yacc
import sys
from Lexer import tokens


#Definimos la gramática
def p_PROGRAMA(p):
    '''PROGRAMA : PROGRAM ID SEMICOLON PROGRAMA2 BLOQUE'''
    p[0] = "EXITO"

def p_PORGRAMA2(p):
    '''PROGRAMA2 : VARS
                   | VACIO'''

def p_VARS(p):
    '''VARS : VAR VARS2'''

def p_VARS2(p):
    '''VARS2 : VARS3 COLON TIPO SEMICOLON'''

def p_VARS3(p):
    '''VARS3 : ID 
            | ID COMMA VARS2'''

def p_TIPO(p):
    '''TIPO : INT
            | FLOAT'''
            
def p_BLOQUE(p):
    '''BLOQUE : BRACKETIZQ ESTATUTO BRACKETDER'''

def p_ESTATUTO(p):
    '''ESTATUTO : ESTATUTO2 ESTATUTO
                | VACIO'''

def p_ESTATUTO2(p):
    '''ESTATUTO2 : ASIGNACION
                | CONDICION
                | ESCRITURA'''

def p_ASIGNACION(p):
    '''ASIGNACION : ID IGUAL EXPRESION SEMICOLON'''

def p_ESCRITURA(p):
    '''ESCRITURA : PRINT PARENIZQ ESCRITURA2 ESCRITURA3 PARENDER SEMICOLON'''

def p_ESCRITURA2(p):
    '''ESCRITURA2 : EXPRESION 
                | CTESTRING'''

def p_ESCRITURA3(p):
    '''ESCRITURA3 : COMMA ESCRITURA2 ESCRITURA3
                | VACIO'''

def p_EXPRESION(p):
    '''EXPRESION : EXP EXPRESION2'''

def p_EXPRESION2(p):
    '''EXPRESION2 : MASQUE EXP
                | MENOSQUE EXP
                | NOIGUAL EXP
                | VACIO'''

def p_CONDICION(p):
    '''CONDICION : IF PARENIZQ EXPRESION PARENDER BLOQUE CONDICION2 SEMICOLON'''

def p_CONDICION2(p):
    '''CONDICION2 : ELSE BLOQUE
                    | VACIO'''

def p_EXP(p):
    '''EXP : TERMINO EXP2'''
    
def p_EXP2(p):
    '''EXP2 : SIMMAS TERMINO EXP2
            | SIMMENOS TERMINO EXP2
            | VACIO'''

def p_TERMINO(p):
    '''TERMINO : FACTOR TERMINO2'''

def p_TERMINO2(p):
    '''TERMINO2 : SIMMULT FACTOR TERMINO2
                | SIMDIV FACTOR TERMINO2
                | VACIO'''

def p_FACTOR(p):
    '''FACTOR : PARENIZQ EXPRESION PARENDER
                | FACTOR2 VARCTE'''

def p_FACTOR2(p):
    '''FACTOR2 : SIMMAS
                | SIMMENOS
                | VACIO'''

def p_VARCTE(p):
    '''VARCTE : ID
                | CTEI
                | CTEF'''

def p_ERROR(p):
    print("Error de sintaxis en  '%s'" % p.value)

def p_VACIO(p):
    '''VACIO : '''
    pass

#Creamos el parser
yacc.yacc()

#En main leemos el archivo y le pasamos los datos al parser
if __name__ == '__main__':

    
        #Le pasamos el nombre del archivo por el command line
        file = "AssetsMyTest.txt"
        tFile = open(file, 'r')
        text = tFile.read()
        tFile.close()
   