import ply.lex as lex #libreria ply de python para analisis lexico
import re #libreria para gestion de expresiones regulares
import codecs #libreria para gestion de ficheros
import os #libreria para uso del sistema
import sys #libreria para uso del sistema

reservadas=['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST','VAR',
'PROCEDURE','OUT','IN','ELSE']#DEFINO ARRAY DE PALABRAS RESERVADAS

tokens=reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','ODD',
'ASSIGN','NE','LT','LTE','GT','GTE','LPARENT','RPARENT','COMMA','SEMMICOLOM',
'DOT','UPDATE']

#tokens=tokens+list(reservadas.values())
#defino el valor en el keywords de cada uno de los tokens
t_ignore='\t'
t_PLUS=r'\+'
t_MINUS=r'\-'
t_TIMES=r'\*'
t_DIVIDE=r'/'
t_ODD=r'ODD'
t_ASSIGN=r'='
t_NE=r'<>'
t_LT=r'<'
t_LTE=r'<='
t_GT=r'>'
t_LPARENT=r'\('
t_RPARENT=r'\)'
t_COMMA=r','
t_SEMMICOLOM=r';'
t_DOT=r'\.'
t_UPDATE=r':='

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'#Evaluo la expresion regular recibida
	if t.value.upper()in reservadas:
		t.value=t.value.upper()#convierte a mayuscula todos los valores de palabras reservadas
		t.type=t.value
	return t
def t_newLine(t):#evalua que el salto de linea no sea reconocido como caracter ilegal
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):#defino el valor inicial para ionsertar un comentario(#)
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int()#casteo el valor del token para que solo reconozca digitos decimales
	return t

def t_error(t):
	print"caracter ilegal'%s'" % t.value[0]#si no cumple con ninguna condicion de las funciones anteriores, se lanza error de caracter ilegal
	t.lexer.skip(1)

def buscarFicheros(directorio):
	ficheros=[]
	numArchivo=''#nos permite listar los archivos que haya en el directorio
	respuesta=False
	cont=1

	for base, dirs, files in os.walk(directorio):#recorre el sistema hasta el directorio actual
		ficheros.append(files)

	for file in files:
		print str(cont)+". "+file
		cont = cont+1

	while respuesta==False:
		numArchivo=raw_input('\n Numero del test:')#una vez retornados la lista de archivo recibe por teclado e mismo a seleccionar
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break
	print "has escogido \"%s\"\n" %files[int(numArchivo)-1]
	return files[int(numArchivo)-1]

directorio = '/home/and1025/Escritorio/files/'#url del directorio de ficheros a evaluar
archivo = buscarFicheros(directorio)
test = directorio + archivo

fp=codecs.open(test,"r","utf-8")#uso de la libreria codecs
cadena = fp.read()
fp.close()

analizador=lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok: break
	print tok
