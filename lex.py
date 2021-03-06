#
# lex.py
# Archivo con el léxico de nuestro compilador
#

import sys
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

#
# Importa el módulo lex de PLY (Python Lex-Yacc)
#

import ply.lex as lex
#
# Lista de tokens:
#   reserved = tokens reservados
#   tokens = todos los otros tokens
#

reserved = {
   'class' : 'CLASS',
   'extends' : 'EXTENDS',
   'global' : 'GLOBAL',
   'int' : 'INT',
   'float' : 'FLOAT',
   'string' : 'STRING',
   'bool' : 'BOOL',
   'void' : 'VOID',
   'if' : 'IF',
   'else' : 'ELSE',
   'for' : 'FOR',
   'while' : 'WHILE',
   'read' : 'READ',
   'print' : 'PRINT',
   'printarr' : 'PRINTARR',
   'int' : 'INT',
   'public' : 'PUBLIC',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'new' : 'NEW',
   'main' : 'MAIN',
   'return' : 'RETURN',
}

tokens = [
   'ID',
   'CTES',
   'CTEI',
   'CTEF',
   'EQUAL',
   'COMMA',
   'OBRACKET',
   'CBRACKET',
   'SEMICOLON',
   'OPARENTHESIS',
   'CPARENTHESIS',
   'PERIOD',
   'PLUSPLUS',
   'MINUSMINUS',
   'OCURLY',
   'CCURLY',
   'PLUS',
   'MINUS',
   'MULT',
   'DIVIDE',
   'OR',
   'AND',
   'MORETHAN',
   'LESSTHAN',
   'NOTEQUAL',
   'EQUALEQUAL',
   ]+list(reserved.values())

variables = []

#
# Expresiones regulares ligadas a los tokens
#

def t_COMMENTS(t):
  r'/\*.*?\*/'
  lexer.skip(1)
  


t_CTEF        = r'[0-9]+\.[0-9]+'
t_CTEI        = r'\d+'
t_CTES        = r'\"[^"\r\n]*\"'
t_EQUAL       = r'='
t_COMMA    		= r','
t_OBRACKET     = r'\['
t_CBRACKET      = r'\]'
t_SEMICOLON     = r'\;'
t_OPARENTHESIS  = r'\('
t_CPARENTHESIS = r'\)'
t_PERIOD        = r'\.'
t_PLUSPLUS    =r'\+\+'
t_MINUSMINUS    =r'\-\-'
t_OCURLY     = r'\{'
t_CCURLY   = r'\}'
t_PLUS    		= r'\+'
t_MINUS        = r'\-'
t_MULT    		= r'\*'
t_DIVIDE    		= r'\/'
t_OR    		= r'\|\|'
t_AND    		= r'\&\&'
t_MORETHAN      = r'\>'
t_LESSTHAN      = r'\<'
t_NOTEQUAL         =r'!='
t_EQUALEQUAL         =r'=='

#
# Expresión regular de los IDs. 
# Confirma que no estén en las palabras reservadas.
#

def t_ID(t):
  r'([a-z]+|[A-Z]+)'
  if t.value in reserved:
    t.type = reserved[ t.value ]
  return t

#
# Ignorar espacios y tabs
#

t_ignore  = ' \t \n \r'

#
# Manejo de errores de léxico
#
def t_error(t):
  print ("Caracter ilegal '%s'" % t.value)
  t.lexer.skip(1)

#
# Construye dos lexer idénticos, para las dos pasadas del parser
# 

lexer = lex.lex()
lexer2 = lex.lex()

#
# Maneja el archivo de entrada, que es el primer argumento del comando en terminal
#

fo = open(sys.argv[1])
str = fo.read();
lexer.input(str)
lexer2.input(str)
