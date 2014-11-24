#
# yacc.py
# Archivo con el léxico de nuestro compilador
#

#
# Importa:
#	- El módulo lex de PLY (Python Lex-Yacc)
#	- Pickle, para guardar a archivo como serie de objetos
#	- Los tokens y dos lexers del archivo lex.py
#


import ply.yacc as yacc
import pickle

from lex import tokens
from lex import lexer
from lex import lexer2

DEBUG = True

contadorMetodos = 0								# Mantiene el número de métodos en la clase actual
contadorVariables = 0							# Mantiene el número de variables en el método actual
tipoRepetida = ""								# Variable que guarda el tipo  para la asignación de variables separadas con comas
listaCuadruplos = []							# La lista que contiene todos los cuádruplos
pilaSaltos = []									# La pila de saltos, que guarda las posiciones para los saltos entre cuadruplos
contCuadruplos = 0								# Variable que contiene el número de cuádruplo actual.
parametros = 0									# Variable que guarda el número de parámetros para el metodo actual.
variablesLocales = 0							# Variable que guarda el número de variables locales (incluyendo parámetros) del metodo
clase = 0										# Variable que guarda el número de clase actual
metodo = 0										# Variable que guarda el número de metodo actual
variable = 0									# Variable que guarda el número de variable actual
printnum = 0									# Variable usada como boleana para sólo una vez los resultados
POper = []										# Pila de operaciones
PilaO = []										# Pila de Operandoms
contParametros = 0								# Contador de parámetros, para comparar si las cantidades son equivalentes
nombreMetodoLlamada = ""						# Variable que guarda el nombre del método a llamar, en el cuádruplo ERA
tablaConstantes=[[40001, "int",'1']]			# La lista de constantes, inicializada con el "1" por propósitos de ++ y --
segundaVuelta = False 							# Variable boleana para la segunda pasada del parser


# 
# Contadores de Variables para Memoria
#

globalInt = 10000
globalFloat = 12501
globalBool = 15001
globalString = 17501
tempInt = 20001
tempFloat = 25001
tempBool = 30001
tempString = 35001
cteInt = 40002
cteFloat = 45001
cteBool = 50001
cteString = 55001

#
# Las siguientes lineas establecen la estructura de nuestra tabla de procedimientos
# - Programa
# ---- name (atributo)
# ---- classes (lista de nodos Clase)
#
# - Clase
# ---- name (atributo)
# ---- methods (lista de nodos Metodo)
# ---- + addMethod(methodType, methodName, numClase) -> añade un metodo a la clase con un tipo, nombre, y el número de método que es
#
# - Metodo
# ---- name (atributo)
# ---- type (atributo)
# ---- variables (lista de nodos Variable)
# ---- numClase (numero de la clase padre)
# ---- numParametros (numero de parametros que tiene)
# ---- numVariables (numero de variables que tiene, incluyendo parametros)
# ---- numCuadruplos (el cuádruplo donde empieza el metodo)
# ---- + setParametersNumber(num) -> Le pone el número de parámetros al método
# ---- + setVariablesNumber(num) -> Le pone el número de variables (incluyendo parámetros) al método
# ---- + setInicioCuadruplosNumber(num) -> Le pone el número de cuádruplo donde empieza el metodo
# ---- + addVariable(variableType, name, numMetodo, numClase, dimension) -> añade una variable al método con un tipo, nombre, y si es dimensionada. Si lo es, guarda su tamaño. Si no, guarda False
# 
# Los tipos de variables a agregar son los siguientes:
# - Ctei
# - Ctef
# - Ctes
# - Cteb
#
# 
# Cada método maneja la lógica para revisar si ya se declaró o no la clase, método o variable.
#

class Expr: pass

class Programa(Expr):
	def __init__(self):
		self.name = "Programa"
		self.classes = []

	def __repr__(self, level=0):
		# ret = "\t"*level+repr(self.name)+"\n"
		# for classInstance in self.classes:
		# 	ret += classInstance.__repr__(level+1)
		# return ret
		ret = [repr(self.name)]
		for classInstance in self.classes:
			ret.append(classInstance.__repr__(level+1))
		return ret

	def __getitem__(self, level=0):
		ret = [repr(self.name)]
		for classInstance in self.classes:
			ret.append(classInstance.__repr__(level+1))
		return ret

class Clase(Expr):
	def __init__(self, name, numClase):
		global contadorMetodos
		for x in range(len(programa.classes)):
			if programa.classes[x].name == name :
				print("Ya existe la clase", name)
				break
		else:
			self.name = name
			self.methods = [Metodo("void", "global", numClase), Metodo("void", "main",numClase)]
			contadorMetodos += 2

	def __repr__(self, level=0):
		ret = [repr(self.name)]
		for method in self.methods:
			ret.append(method.__repr__(level+1))
		return ret

	def addMethod(self, methodType, methodName, numClase):
		self.methods.append(Metodo(methodType, methodName,numClase))

class Metodo(Expr):
	def __init__(self, methodType, name, numClase):
		global contadorMetodos
		if contadorMetodos < 2:
			self.type = methodType
			self.name = name
			self.variables = []
			self.numClase= numClase
			self.numParametros = 0
			self.numVariables = 0
			self.numCuadruplos = 0
		else:
			for x in range(len(programa.classes[numClase].methods)):
				if programa.classes[numClase].methods[x].name == name :
					print("Ya existe el metodo", name)
					break
			else:
				self.type = methodType
				self.name = name
				self.variables = []
				self.numClase= numClase
				self.numParametros = 0
				self.numVariables = 0
				self.numCuadruplos = 0

	def __repr__(self, level=0):
		ret = [repr(self.name), repr(self.type), repr(self.numParametros), repr(self.numVariables),repr(self.numCuadruplos)]
		for variable in self.variables:
			ret.append(variable.__repr__(level+1))
		return ret

	def setParametersNumber(self, num):
		self.numParametros = num

	def setVariablesNumber(self, num):
		self.numVariables = num

	def getVariablesNumber(self):
		return self.numVariables

	def setInicioCuadruplosNumber(self, num):
		self.numCuadruplos = num

	def addVariable(self, variableType, name, numMetodo, numClase, dimension):
		global contadorVariables
		if contadorVariables < 1:
			if variableType == "int":
				self.variables.append(Ctei(name, dimension))

			if variableType == "float":
				self.variables.append(Ctef(name, dimension))

			if variableType == "string":
				self.variables.append(Ctes(name, dimension))

			if variableType == "bool":
				self.variables.append(Cteb(name, dimension))

			contadorVariables +=1

		else:
			for x in range(len(programa.classes[numClase].methods[0].variables)):
				if programa.classes[numClase].methods[0].variables[x].name == name :
					print("Ya existe la variable", name)
					break
			else:
				for x in range(len(programa.classes[numClase].methods[numMetodo].variables)):
					if programa.classes[numClase].methods[numMetodo].variables[x].name == name:
						print("Ya existe la variable", name)
						break
				else:
					if variableType == "int":
						self.variables.append(Ctei(name, dimension))

					if variableType == "float":
						self.variables.append(Ctef(name, dimension))

					if variableType == "string":
						self.variables.append(Ctes(name, dimension))

					if variableType == "bool":
						self.variables.append(Cteb(name, dimension))
					global variablesLocales
					variablesLocales += 1

class Ctei(Expr):
	def __init__(self, name, dimension):
		global globalInt
		global tempInt
		self.type = "int"
		self.name = name
		self.dimension = dimension
		if dimension is False:
			if metodo is 0:
				self.numDir = globalInt
				globalInt += 1
			else:
				self.numDir = tempInt
				tempInt += 1
		else:
			if metodo is 0:
				self.numDir = globalInt
				globalInt += dimension
			else:
				self.numDir = tempInt
				tempInt += dimension

	def __repr__(self, level=0):
		ret = [repr(self.name), repr(self.type), repr(self.numDir), repr(self.dimension)]
		return ret

class Ctef(Expr):
	def __init__(self,name, dimension):
		global globalFloat
		global tempFloat
		self.type = "float"
		self.name = name
		self.dimension = dimension
		if dimension is False:
			if metodo is 0:
				self.numDir = globalFloat
				globalFloat += 1
			else:
				self.numDir = tempFloat
				tempFloat += 1
		else:
			if metodo is 0:
				self.numDir = globalFloat
				globalFloat += dimension
			else:
				self.numDir = tempFloat
				tempFloat += dimension

	def __repr__(self, level=0):
		ret = [repr(self.name), repr(self.type), repr(self.numDir), repr(self.dimension)]
		return ret

class Ctes(Expr):
	def __init__(self,name, dimension):
		global globalString
		global tempString
		self.type = "string"
		self.name = name
		self.dimension = dimension
		if dimension is False:
			if metodo is 0:
				self.numDir = globalString
				globalString += 1
			else:
				self.numDir = tempString
				tempString += 1
		else: 
			if metodo is 0:
				self.numDir = globalString
				globalString += dimension
			else:
				self.numDir = tempString
				tempString += dimension

	def __repr__(self, level=0):
		ret = [repr(self.name), repr(self.type), repr(self.numDir), repr(self.dimension)]
		return ret

class Cteb(Expr):
	def __init__(self,name, dimension):
		global globalBool
		global tempBool
		self.type = "bool"
		self.name = name
		self.dimension = dimension
		if dimension is False:
			if metodo is 0:
				self.numDir = globalBool
				globalBool += 1
			else:
				self.numDir = tempBool
				tempBool += 1
		else: 
			if metodo is 0:
				self.numDir = globalBool
				globalBool += dimension
			else:
				self.numDir = tempBool
				tempBool += dimension


	def __repr__(self, level=0):
		ret = [repr(self.name), repr(self.type), repr(self.numDir), repr(self.dimension)]
		return ret

#
# rellenar
# - acambiar (cuádruplo a cambiar)
# - aponer (la dirección a poner)
#
# El método rellena el cuadrúpolo dado con la dirección dada. Usado en "goto"s, etc.
#

def rellenar(acambiar,aponer):
	listaCuadruplos[acambiar].append(str(aponer))

#
# Inicializa la estructura Programa, detallada arriba, en la variable "programa"
#

programa = Programa()

#
# Inicia la Sintaxis
# 
# Todas los metodos siguientes, identificados por la estructura "p_NOMBRE(p)" son usados
# por PLY para la generación del parser. Debajo de cada metodo están las instrucciones a 
# correr cuando la sintaxis dada termine. Es decir, ese código se corre cuando se encuentre
# y consuma correctamente el léxico en la sintaxis dada.
#


#
# Clase
#
# Siendo el primer elemento de la sintaxis, y por ende, el último método en 
# ser completado y ejecutado, sus instrucciones son las últimas en correrse.
#
# Hace lo siguiente:
# - Imprime a consola la tabla de procedimientros
# - Imprime la tabla de constantes
# - Si es la segunda vuelta:
# ---- Imprime los cuádruplos
# ---- Imprime a archivo, que se llamará "codigo.txt"
#

def p_clase(p):
	'clase : CLASS clase_a a'
	global printnum
	if printnum == 0:
		print(programa[0])
		printnum = printnum +1
		print ("\n")
		print (tablaConstantes)
		if segundaVuelta == True:
			for x in range(len(listaCuadruplos)):
				print( str(x) + " " + str(listaCuadruplos[x]) + "\n")
			print(PilaO)
			output = open('codigo.txt', "wb")
			# file.write(str(programa[0]) + "\n" + str(tablaConstantes) + "\n" + str(listaCuadruplos))
			pickle.dump([programa[0], tablaConstantes, listaCuadruplos],output)
			output.close()

#
#  clase_a
#
# Inicializa el contador de métodos, y agrega la clase a la tabla de procedimientos
#

def p_clase_a(p):
	'clase_a : ID'
	global clase
	global contadorMetodos
	contadorMetodos = 0
	programa.classes.append(Clase(p[1], clase))

#
# a
#
# Da la opción de que la clase sea hija de otra
# 
# REVISAR REVISAR REVISAR REVISAR REVISAR REVISAR
# REVISAR REVISAR REVISAR REVISAR REVISAR REVISAR
# REVISAR REVISAR REVISAR REVISAR REVISAR REVISAR
#

def p_a(p):
	'''a : EXTENDS ID b
		| b'''

def p_b(p):
	'b : OCURLY programa CCURLY bb'

def p_bb(p):
	'''bb : incclase clase
		| '''

#
# incclase
#
# Significa una clase acabó y otra empezó. Actualiza el contador de 
# clases y resetea el contador de metodos
#

def p_incclase(p):
	'''incclase : '''
	global clase
	global metodo
	clase = clase + 1
	metodo = 0

def p_programa(p):
	'programa : c'


def p_c(p):
	'''c : ID ID EQUAL NEW creaobj c
		| ddd
		| e'''

def p_d(p):
	'd : ddddd vars dd'

def p_ddd(p):
	'ddd : dddd d'

def p_dddd(p):
	'dddd : '

def p_ddddd(p):
	'ddddd : GLOBAL'


def p_dd(p):
	'''dd : d
		| main e'''

def p_e(p):
	'e : ee'

def p_ee(p):
	'''ee : metodos eee
		| '''
	

def p_eee(p):
	'''eee : ee
		| '''

def p_creaobj(p):
	'creaobj : ID OPARENTHESIS CPARENTHESIS SEMICOLON'

def p_vars(p):
	'vars : f'

def p_f(p):
	'''f : PUBLIC g
			| g'''

#
# g
#
# Guarda el tipo que se usará en la variable o variables.
# Añade la variable a la clase y método donde se encuentra.
#

def p_g(p):
	'g : tipo h'
	global clase
	global metodo
	global tipoRepetida
	tipoRepetida = p[1]
	if p[2][1] == False:
		programa.classes[clase].methods[metodo].addVariable(p[1], p[2][0], metodo, clase, False)
	else:
		programa.classes[clase].methods[metodo].addVariable(p[1], p[2][0], metodo, clase, p[2][1])

#
# h
#
# Regresa a g el nombre de la variable, y el tamaño si es dimensionada
#

def p_h(p):
	'h : ID i'
	if p[2][1] == True:
		p[0] = [p[1], p[2][0]] 
	else:
		p[0] = [p[1], False]

#
# i
#
# Manejo de variables dimensionadas
#

def p_i(p):
	'''i : OBRACKET CTEI CBRACKET j
		| j'''
	if len(p) == 5:
		if int(p[2]) > 0:
			p[0] = [int(p[2]), True]
	if len(p) == 2:
		p[0] = [p[1], False]
		

#
# j
#
# Si hay más variables despues de la coma, las regresa
#

def p_j(p):
	'''j : COMMA j_j
		| SEMICOLON'''
	if len(p) == 3:
		p[0] = p[2]

#
# j_j
#
# Agrega la variable a la lista de procedimientos
#

def p_j_j(p):
	'''j_j : ID j'''
	global clase
	global metodo
	programa.classes[clase].methods[metodo].addVariable(tipoRepetida, p[1], metodo, clase,False)

#
# tipo
#
# Regresa el tipo de la variable
#

def p_tipo(p):
	'''tipo : INT
		| FLOAT
		| BOOL
		| STRING'''
	p[0] = p[1]
	global tipoRepetida
	tipoRepetida = p[1]

#
# checaSiExiste
#
# Metodo simple que busca un elemento dentro de la tabla de constantes
# Si lo encuentra, lo regresa al que lo llamó. Si no, regresa False.
#

def checaSiExiste(elemento):
	if len(tablaConstantes) < 1:
		return False
	else:
		for a in range(len(tablaConstantes)):
			if elemento == tablaConstantes[a][2]:
				return tablaConstantes[a]
				break;
		else:
			return False

#
# checaSiExisteVariables
#
# De igual forma, este metodo busca si ya existe la variable.
# Si existe, la regresa. Si no, regresa falso.
#

def checaSiExisteVariables(elemento):
	global clase
	global metodo

	if len(programa.classes[clase].methods[metodo].variables) < 1:
		return False
	else:
		for a in range(len(programa.classes[clase].methods[metodo].variables)):
			if elemento == programa.classes[clase].methods[metodo].variables[a].name:
				return [programa.classes[clase].methods[metodo].variables[a].numDir, programa.classes[clase].methods[metodo].variables[a].type, programa.classes[clase].methods[metodo].variables[a].name]
				break;
		else:
			return False


#
# varcte
#
# Revisa el tipo de VARCTE. Si es una variable constante, la agrega a la lista de constantes.
#

def p_varcte(p):
	'''varcte : CTEI varcte_int
		| CTEF varcte_float
		| CTES varcte_string
		| FALSE varcte_bool
		| TRUE varcte_bool
		| varcte_id'''
	global cteInt
	global cteFloat
	global cteBool
	global cteString
	if len(p) == 3:
		#tablaConstantes.append([p[1], p[2]])
		#p[0] = [p[1], p[2]]
	#
	# Esto se comento porque ya asignan direcciones a constantes
	#
		if p[2] == "int":
			if checaSiExiste(p[1]) == False:
				aux = cteInt
				p[0] = [aux, p[2], p[1]]
				tablaConstantes.append([aux, p[2], p[1]])
				cteInt +=1
			else:
				p[0] = checaSiExiste(p[1])
		elif p[2] == "float":
			if checaSiExiste(p[1]) == False:
				aux = cteFloat
				p[0] = [aux, p[2], p[1]]
				tablaConstantes.append([aux, p[2], p[1]])
				cteFloat +=1
			else:
				p[0] = checaSiExiste(p[1])
		elif p[2] == "bool":
			if checaSiExiste(p[1]) == False:
				aux = cteBool
				p[0] = [aux, p[2], p[1]]
				tablaConstantes.append([aux, p[2], p[1]])
				cteBool +=1
			else:
				p[0] = checaSiExiste(p[1])
		elif p[2] == "string":
			if checaSiExiste(p[1]) == False:
				aux = cteString
				p[0] = [aux, p[2], p[1]]
				tablaConstantes.append([aux, p[2], p[1]])
				cteString +=1
			else:
				p[0] = checaSiExiste(p[1])

	# REVISAR REVISAR REVISAR REVISAR REVISAR REVISAR
	# REVISAR REVISAR REVISAR REVISAR REVISAR REVISAR
	# REVISAR REVISAR REVISAR REVISAR REVISAR REVISAR

	if len(p) == 2:	
		print("Este de arriba es listatemp")
		listatemp = checaSiExisteVariables(p[1][0])
		print (listatemp)
		if listatemp is not False:
			p[0] = listatemp

def p_varcte_int(p):
	'''varcte_int : '''
	p[0] = "int"

def p_varcte_float(p):
	'''varcte_float : '''
	p[0] = "float"

def p_varcte_string(p):
	'''varcte_string : '''
	p[0] = "string"

def p_varcte_bool(p):
	'''varcte_bool : '''
	p[0] = "bool"

#
# varcte_id
#
# Si lo que se recibió es una variable, la busca en el metodo. Si la encuentra, la regresa.
# Si no, la busca en las variables globales. Si la encuentra, la regresa. Si no, da el mensaje de que no se encontró.
#


def p_varcte_id(p):
	'''varcte_id : ID'''
	global clase
	global metodo
	for x in range(len(programa.classes[clase].methods[metodo].variables)):
		if programa.classes[clase].methods[metodo].variables[x].name == p[1]:
			p[0] = [programa.classes[clase].methods[metodo].variables[x].name, programa.classes[clase].methods[metodo].variables[x].type]
			break;
		elif x == len(programa.classes[clase].methods[metodo].variables)-1:
			for y in range(len(programa.classes[clase].methods[0].variables)):
				if programa.classes[clase].methods[0].variables[y].name == p[1]:
					p[0] = [programa.classes[clase].methods[0].variables[y].name, programa.classes[clase].methods[0].variables[y].type]
					break;
				elif x == len(programa.classes[clase].methods[0].variables)-1:
					print("No se encontro la variable", p[1], " ", clase, " ", metodo)

def p_metodos(p):
	'''metodos : k'''
	global variablesLocales
	variablesLocales = 0

def p_k(p):
	'k : k_k OPARENTHESIS l'

#
# k_k
#
# Agrega el metodo a la clase, y actualiza el contador del metodo y de variables, asi como el de parametros.
#

def p_k_k(p):
	'''k_k : tipo ID
			| VOID ID'''
	global clase
	global metodo
	global parametros
	tipo = p[1]
	programa.classes[clase].addMethod(p[1], p[2], clase)
	metodo = metodo + 1
	contadorVariables = 0
	parametros = 0

def p_l(p):
	'''l : pars actualizaparametros ll
		| ll'''

#
# actualizaparametros
#
# Al terminar la declaracion de parametros, actualiza el metodo con la cantidad de ellos
#
def p_actualizaparametros(p):
	'actualizaparametros : '
	global parametros
	global clase
	global metodo
	programa.classes[clase].methods[metodo].setParametersNumber(parametros)

def p_ll(p):
	'll : CPARENTHESIS OCURLY poncuadruplometodo m'

def p_m(p):
	'm : vars terminavarsmetodo mm'

#
# terminavarsmetodo
#
# Al igual que arriba, actualiza el metodo con la cantidad de variables en el (incluyendo parametros)
#

def p_terminavarsmetodo(p):
	'terminavarsmetodo : '
	global variablesLocales
	global clase
	global metodo
	programa.classes[clase].methods[metodo].setVariablesNumber(variablesLocales)
	variables = 0



def p_mm(p):
	'''mm : estatuto n
		| m'''

#
# poncuadruplometodo
#
# Otra vez, actualiza el número de inicio de cuádruplo del método
#

def p_poncuadruplometodo(p):
	'poncuadruplometodo : '
	global contCuadruplos
	programa.classes[clase].methods[metodo].setInicioCuadruplosNumber(contCuadruplos)

def p_n(p):
	'''n : CCURLY 
		| mm'''

	global variablesLocales
	global clase
	global metodo
	tipo = programa.classes[clase].methods[metodo].type
	programa.classes[clase].methods[metodo].addVariable(tipo, "return", metodo, clase, False)
	print("REEEEEEEEEEETURN")



#
# checaSiExistePars
#
# Regresa la dimension de la variable, si es que tiene.
#
#

def checaSiExistePars(elemento):
	global clase
	global metodo

	if len(programa.classes[clase].methods[metodo].variables) < 1:
		return False
	else:
		for a in range(len(programa.classes[clase].methods[metodo].variables)):
			if elemento == programa.classes[clase].methods[metodo].variables[a].name:
				return programa.classes[clase].methods[metodo].variables[a].dimension
				break;
		else:
			return False

def p_pars(p):
	'pars : tipo ID o'
	global clase
	global metodo
	global parametros
	programa.classes[clase].methods[metodo].addVariable(p[1], p[2], metodo, clase, checaSiExistePars(p[2]))
	parametros += 1

def p_o(p):
	'''o : OBRACKET CBRACKET oo
		| oo'''

def p_oo(p):
	'''oo : COMMA pars
		| '''

def p_estatuto(p):
	'''estatuto : asignacion
		| IF condicion
		| FOR ciclofor
		| WHILE ciclowhile
		| iniciacontadormetodos prefunc 
		| READ read
		| PRINT print
		| ID PERIOD llamaobj
		| RETURN ssexp SEMICOLON '''
	global metodo
	global clase
	if len(p) == 4:
		if metodo != 1:
			global contCuadruplos
			listaCuadruplos.append(["retorno",PilaO.pop()[0] , metodo, clase])
			listaCuadruplos.append(["RET","","",""])
			contCuadruplos += 2

		else: 
			print ("Return en main!!!!")




def p_iniciacontadormetodos(p):
	'iniciacontadormetodos : ID OPARENTHESIS'
	global nombreMetodoLlamada
	global contCuadruplos
	parametros = 1
	if segundaVuelta == True:
		nombreMetodoLlamada = p[1]

#
# asignacion
#
# Genera el cuadruplo de asignacion, si es simple. Si es de ++ p --, genera directamente el cuadruplo,
# sin sacar de la pila.
#

def p_asignacion(p):
	'''asignacion : variable EQUAL meteequal expresion SEMICOLON
			| ID asig_a SEMICOLON
			| OBRACKET variable EQUAL meteequal iniciacontadormetodos prefunc CBRACKET'''
	global contCuadruplos
	if len(p) == 6:
		try:
			if(p[1] is not None and p[4][0]):
				a = PilaO.pop()
				print("\n \n Saco %s de la pila en la asignacion \n\n" % a[0])
				PilaO.append(a)
				listaCuadruplos.append(["=", PilaO.pop()[0], "", p[1][0]])
				contCuadruplos += 1
		except IndexError:
			b = 'IndexError'
	elif len(p) == 4: 
		global clase
		global metodo
		for x in range(len(programa.classes[clase].methods[metodo].variables)):
			if programa.classes[clase].methods[metodo].variables[x].name == p[1] and programa.classes[clase].methods[metodo].variables[x].type == "int":
				global tempInt
				if p[2] == '++':
					listaCuadruplos.append(["++", programa.classes[clase].methods[metodo].variables[x].numDir, 40001, programa.classes[clase].methods[metodo].variables[x].numDir])
				if p[2] == '--':
					listaCuadruplos.append(["--", programa.classes[clase].methods[metodo].variables[x].numDir, 40001, programa.classes[clase].methods[metodo].variables[x].numDir])
				contCuadruplos +=1
		else: 
			print("INTENTASTE UN MASMAS O MENOSMENOS Y NO ERA INT")
	elif len(p) == 8:
		if segundaVuelta == True:
			try:
				if(p[2] is not None and p[6][0]):
					a = PilaO.pop()
					print("\n \n Saco %s de la pila en la asignacion de prefunc\n\n" % a[0])
					PilaO.append(a)
					listaCuadruplos.append(["=", PilaO.pop()[0], "", p[2][0]])
					contCuadruplos += 1
			except IndexError:
				b = 'IndexError'

def p_meteequal(p):
	'meteequal : '
	POper.append("=")

def p_asig_a(p):
	'''asig_a : PLUSPLUS
			| MINUSMINUS '''
	p[0] = p[1]

#
# condicion
#
# Al terminar la condicion, saca una direccion de cuadruplo de la pila saltos y le actualiza la direccion
# a la que tiene que saltar.
#

def p_condicion(p):
	'condicion : OPARENTHESIS ssexp CPARENTHESIS ponergotoif bloque p'
	global contCuadruplos
	rellenar(pilaSaltos.pop(), contCuadruplos)

#
# GOTO
#
# La mayoria de las instrucciones siguientes estan relacionadas con la actualizacion
# correcta de los cuadruplos con lo especificado en la pila de saltos
#


def p_ponergotoif(p):
	'ponergotoif : '
	global contCuadruplos
	aux = PilaO.pop()
	listaCuadruplos.append(["gotof", aux[0], ""])
	contCuadruplos += 1
	pilaSaltos.append(contCuadruplos-1)

def p_p(p):
	'''p : ELSE gotoelse pp
		| '''

def p_gotoelse(p):
	'gotoelse : '
	global contCuadruplos
	listaCuadruplos.append(["goto", "", ""])
	contCuadruplos += 1
	rellenar(pilaSaltos.pop(), contCuadruplos)
	pilaSaltos.append(contCuadruplos-1)

def p_pp(p):
	'''pp : IF condicion
		| bloque'''

def p_ciclofor(p):
	'ciclofor : iniciafor OPARENTHESIS parfor CPARENTHESIS gotoffor bloque'
	global contCuadruplos
	falso  = pilaSaltos.pop()
	retorno = pilaSaltos.pop()
	listaCuadruplos.append(["goto", "", "", retorno + 1])
	contCuadruplos += 1
	rellenar(falso, contCuadruplos)

def p_iniciafor(p):
	'iniciafor : '
	global contCuadruplos
	pilaSaltos.append(contCuadruplos)

def p_gotoffor(p):
	'gotoffor : '
	global contCuadruplos
	aux = PilaO.pop()
	print(aux) 
	print(int(aux[0])-1) 
	listaCuadruplos.append(["gotov", aux[0], ""])
	contCuadruplos += 1
	pilaSaltos.append(contCuadruplos-1)

def p_ciclowhile(p):
	'ciclowhile : iniciawhile OPARENTHESIS ssexp CPARENTHESIS gotofwhile bloque'
	global contCuadruplos
	falso  = pilaSaltos.pop()
	retorno = pilaSaltos.pop()
	listaCuadruplos.append(["goto", "", "", retorno])
	contCuadruplos += 1
	rellenar(falso, contCuadruplos)

def p_iniciawhile(p):
	'iniciawhile : '
	global contCuadruplos
	pilaSaltos.append(contCuadruplos)

def p_gotofwhile(p):
	'gotofwhile : '
	global contCuadruplos
	aux = PilaO.pop()
	listaCuadruplos.append(["gotof", aux[0], ""])
	contCuadruplos += 1
	pilaSaltos.append(contCuadruplos-1)

#
# prefunc
#
# Esta funcion maneja las llamadas a metodos. Solo se corre cuando es la segunda vuelta del parser, ya que
# en la primera no se ha generado completa la tabla de procedimientos.
#

def p_prefunc(p):
	'''prefunc : q
			| rrr'''
	if segundaVuelta is True:
		global contParametros
		global contCuadruplos
		cont = 1
		for x in range(len(programa2.classes[clase].methods)):
			if programa2.classes[clase].methods[x].name == nombreMetodoLlamada:
				listaCuadruplos.append(["ERA", nombreMetodoLlamada, clase,""])
				contCuadruplos+=1
				if programa2.classes[clase].methods[x].numParametros == contParametros:
					for y in range(programa2.classes[clase].methods[x].numParametros):
						aux1 = PilaO.pop()
						aux2 = programa2.classes[clase].methods[x].variables[y].type
						if aux1[1] == aux2:
							print ("Los tipos", aux1[1], "y", aux2, "son iguales")
							listaCuadruplos.append(["param", aux1[0], "", "param"+str(cont)])
							contCuadruplos += 1
							cont += 1
						else:
							print("ERROR DE TIPOS EN EL PARAMETRO", aux1, "", aux2)
							break;
					else:
						listaCuadruplos.append(["GOSUB", nombreMetodoLlamada, clase, ""])
						contCuadruplos += 1
						PilaO.append([programa2.classes[clase].methods[x].variables[len(programa2.classes[clase].methods[x].variables)-1].numDir, programa2.classes[clase].methods[x].type]) 
						p[0] = [programa2.classes[clase].methods[x].variables[len(programa2.classes[clase].methods[x].variables)-1].numDir, programa2.classes[clase].methods[x].type]

				else:
					print ("No concuerda el numero de parametros", programa2.classes[clase].methods[x].numParametros, " no es igual a ", contParametros)
				break;
		else:
			print ("El metodo llamado no existe")
		contParametros = 0

def p_q(p):
	'q : exp r'
	global contParametros
	contParametros += 1

def p_r(p):
	'''r : OBRACKET CBRACKET
		| rr'''

def p_rr(p):
	'''rr : COMMA q
		| rrr'''

def p_rrr(p):
	'rrr : CPARENTHESIS SEMICOLON'

def p_read(p):
	'read : OPARENTHESIS CPARENTHESIS SEMICOLON'

def p_print(p):
	'print : OPARENTHESIS exp CPARENTHESIS SEMICOLON'
	global contCuadruplos
	listaCuadruplos.append(["print", p[2][0],"", ""])
	print("print", p[2][0],", , ")
	contCuadruplos+=1

def p_llamaobj(p):
	'llamaobj :  ID s'

def p_s(p):
	'''s : SEMICOLON
		| ss'''

def p_ss(p):
	'ss : OPARENTHESIS sss CPARENTHESIS SEMICOLON'

def p_sss(p):
	'''sss : exp
		| '''

#
# variable
#
# Este metodo busca la variable en el metodo regresa la direccion de la variable y el tipo.
# En el caso de que sea un arreglo, regresa la posición exacta dentro de la estructura del arreglo
# a la que se quiera accesar.
#

def p_variable(p):
	'variable : ID t'
	global clase
	global metodo
	for x in range(len(programa.classes[clase].methods[metodo].variables)):
		if programa.classes[clase].methods[metodo].variables[x].name == p[1]:
			temp = programa.classes[clase].methods[metodo].variables[x].numDir + int(p[2])			
			p[0] = [temp, programa.classes[clase].methods[metodo].variables[x].type]
			break;
		elif x == len(programa.classes[clase].methods[metodo].variables)-1:
			print("No se encontro la variable", p[1], " ", clase, " ", metodo)

def p_t(p):
	'''t : OBRACKET CTEI CBRACKET
		| PERIOD ID
		|  '''
	if len(p) == 4:
		p[0] = p[2]
	else:
		p[0] = 0


def p_expresion(p):
	'expresion : ssexp'
	p[0] = p[1]

def p_ssexp(p):
	'''ssexp : sexp u'''
	p[0] = p[1]

def p_u(p):
	'''u : meteapilaandor ssexp checapilaorand
		| '''

#
# METE A PILA
#
# Los metodos siguientes tratan sobre el ingreso a la pila de 
# operadores, con la estructura sintáctica proveyendo la prioridad y jerarquía.
#

def p_meteapilaandor(p):
	'''meteapilaandor : AND
					| OR '''
	POper.append(p[1]) 

def p_checapilaorand(p):
	'checapilaorand : '
	global contCuadruplos
	if POper:
		a = POper.pop()
		if a == '&&' or a == '||':
			op = a
			#print(PilaO)
			opdo2 = PilaO.pop()
			opdo1 = PilaO.pop()
			if(opdo1 is not None and opdo2 is not None):
				if (opdo1[1] == opdo2[1]):
					global tempInt
					global tempFloat
					global tempBool
					global tempString
					if opdo1[1] == "int":
						aux = tempInt
						tempInt += 1
					elif opdo1[1] == "float":
						aux = tempFloat
						tempFloat += 1
					elif opdo1[1] == "bool":
						aux = tempBool
						tempBool += 1
					elif opdo1[1] == "string":
						aux = tempString
						tempString += 1
					listaCuadruplos.append([op, opdo1[0], opdo2[0], aux])
					PilaO.append([aux, opdo1[1]])
					contCuadruplos += 1
				else:
					print("ERROR DE TIPOS:", opdo1[1], "y", opdo2[1], " no son iguales")
		else:
			POper.append(a)

def p_sexp(p):
	'sexp : exp v_v'
	p[0] = p[1]

def p_v_v(p):
	'''v_v : v sexp checapilacondicional 
		| '''


def p_checapilacondicional(p):
	'checapilacondicional : '
	global contCuadruplos
	if POper:
		a = POper.pop()
		if a == '>' or a == '<' or a == '>=' or a == '<=' or a == '!=' or a == '==':
			op = a
			#print(PilaO)
			opdo2 = PilaO.pop()
			opdo1 = PilaO.pop()
			if(opdo1 is not None and opdo2 is not None):
				if (opdo1[1] == opdo2[1]):
					global tempInt
					global tempFloat
					global tempBool
					global tempString
					if opdo1[1] == "int":
						aux = tempInt
						tempInt += 1
					elif opdo1[1] == "float":
						aux = tempFloat
						tempFloat += 1
					elif opdo1[1] == "bool":
						aux = tempBool
						tempBool += 1
					elif opdo1[1] == "string":
						aux = tempString
						tempString += 1
					listaCuadruplos.append([op, opdo1[0], opdo2[0], aux])
					PilaO.append([aux, opdo1[1]])
					contCuadruplos +=1
				else:
					print("ERROR DE TIPOS:", opdo1[1], "y", opdo2[1], " no son iguales")
		else:
			POper.append(a)

def p_v(p):
	'''v : MORETHAN w
		| LESSTHAN w
		| NOTEQUAL
		| EQUALEQUAL
		| '''
	if len(p) == 3:
		if p[2] is None:
			POper.append(str(p[1]))
		else:
			POper.append((str(p[1] + str(p[2]))))
	if len(p) == 2:
		POper.append(str(p[1]))

def p_w(p):
	'''w : EQUAL
		| '''
	if len(p) == 2:
		p[0] = p[1]

def p_exp(p):
	'exp : termino checapilamas x'
	p[0] = p[1]

def p_checapilamas(p):
	'checapilamas : '
	global contCuadruplos
	if POper:
		a = POper.pop()
		if a == '+' or a == '-':
			op = a
			opdo2 = PilaO.pop()
			opdo1 = PilaO.pop()
			if(opdo1 is not None and opdo2 is not None):
				if (opdo1[1] == opdo2[1]):
					global tempInt
					global tempFloat
					global tempBool
					global tempString
					if opdo1[1] == "int":
						aux = tempInt
						tempInt += 1
					elif opdo1[1] == "float":
						aux = tempFloat
						tempFloat += 1
					elif opdo1[1] == "bool":
						aux = tempBool
						tempBool += 1
					elif opdo1[1] == "string":
						aux = tempString
						tempString += 1
					listaCuadruplos.append([op, opdo1[0], opdo2[0], aux])
					PilaO.append([aux, opdo1[1]])
					contCuadruplos += 1
				else:
					print("ERROR DE TIPOS:", opdo1[1], "y", opdo2[1], " no son iguales")
		else:
			POper.append(a)

def p_x(p):
	'''x : meteapilamas exp
		| '''

def p_meteapilamas(p):
	'''meteapilamas : PLUS
					| MINUS '''
	POper.append(p[1])

def p_termino(p):
	'termino : factor checapilapor y'
	p[0] = p[1]

def p_checapilapor(p):
	'checapilapor : '
	global contCuadruplos
	if POper:
		a = POper.pop()
		if a == '*' or a == '/':
			op = a
			opdo2 = PilaO.pop()
			opdo1 = PilaO.pop()
			if(opdo1 is not None and opdo2 is not None):
				if (opdo1[1] == opdo2[1]):
					global tempInt
					global tempFloat
					global tempBool
					global tempString
					if opdo1[1] == "int":
						aux = tempInt
						tempInt += 1
					elif opdo1[1] == "float":
						aux = tempFloat
						tempFloat += 1
					elif opdo1[1] == "bool":
						aux = tempBool
						tempBool += 1
					elif opdo1[1] == "string":
						aux = tempString
						tempString += 1
					listaCuadruplos.append([op, opdo1[0], opdo2[0], aux])
					PilaO.append([aux, opdo1[1]])
					contCuadruplos += 1
				else:
					print("ERROR DE TIPOS")
		else:
			POper.append(a)

def p_y(p):
	'''y : meteapilapor termino
		| '''

def p_meteapilapor(p):
	'''meteapilapor : MULT
				| DIVIDE'''
	POper.append(p[1])

def p_factor(p):
	'factor : z'
	p[0] = p[1]

def p_z(p):
	'''z : OPARENTHESIS expresion CPARENTHESIS
		| PLUS zz
		| MINUS zz
		| zz'''
	if len(p) == 4:
		p[0] = p[2]
	if len(p) == 3:
		p[0] = p[2]
	if len(p) == 2:
		p[0] = p[1]

#
# zz
#
# Regresa la direccion de la variable dada asi como su tipo, ademas de meterla a la pila de operandos
#


def p_zz(p):
	'zz : varcte'
	global clase
	global metodo
	for a in range(len(programa.classes[clase].methods[metodo].variables)):
		if p[1][0] == programa.classes[clase].methods[metodo].variables[a].numDir:
			p[0] = [programa.classes[clase].methods[metodo].variables[a].numDir, programa.classes[clase].methods[metodo].variables[a].type]
			break;
	p[0] = p[1]
	PilaO.append(p[1])

def p_bloque(p):
	'bloque : OCURLY a_a CCURLY'

def p_a_a(p):
	'''a_a : estatuto a_a
		| '''

#
# parfor
#
# Esta funcion trata con los parametros del ciclo for.
#
#


def p_parfor(p):
	'parfor : asignacion ssexp SEMICOLON ID b_b'
	global contCuadruplos
	global cteInt
	aux = checaSiExisteVariables(p[4])
	if aux is not False:
		if aux[1] == "int":
			if p[5] == '++':
				listaCuadruplos.append(["++", aux[0], 40001, aux[0]] )
			if p[5] == '--':
				listaCuadruplos.append(["--", aux[0], 40001, aux[0]] )
			contCuadruplos +=1
		temp = listaCuadruplos[len(listaCuadruplos)-2]
		temp2 = listaCuadruplos[len(listaCuadruplos)-1]
		listaCuadruplos[len(listaCuadruplos)-2] = temp2
		listaCuadruplos[len(listaCuadruplos)-1] = temp

def p_b_b(p):
	'''b_b : PLUSPLUS
		| MINUSMINUS'''
	p[0] = p[1]

def p_main(p):
	'main : VOID entroamain MAIN OPARENTHESIS CPARENTHESIS OCURLY c_c CCURLY'
	global variablesLocales
	global contCuadruplos
	variablesLocales = 0
	listaCuadruplos.append(["END","","",""])
	contCuadruplos+=1


def p_entroamain(p):
	'entroamain : '
	global metodo
	print("\n Aumento el metodo de", metodo, "a", metodo+1, "\n")
	metodo = metodo + 1

def p_c_c(p):
	'c_c : cccc ccc'

def p_ccc(p):
	'''ccc : vars ccc
		| d_d'''

def p_cccc(p):
	'cccc : '

def p_d_d(p):
	'd_d : estatuto d_dd'
	

def p_d_dd(p):
	'''d_dd : d_d
		| '''

def p_error(p):
	if p:
		print ("Syntax error at '%s'" % p.value)
	else:
		print ("Syntax error at EOF %s" % p)

# Se crea el primer parser

p = yacc.yacc()

p.parse(lexer=lexer)

# Se resetean las variables necesarias para la segunda vuelta

segundaVuelta = True
clase = 0 
metodo = 0
variable = 0
printnum = 0 
listaCuadruplos	= []
tablaConstantes = [[40001, "int",'1']]
contCuadruplos =0
contParametros = 0

globalInt = 10000
globalFloat = 12501
globalBool = 15001
globalString = 17501
tempInt = 20001
tempFloat = 25001
tempBool = 30001
tempString = 35001
cteInt = 40002
cteFloat = 45001
cteBool = 50001
cteString = 55001

#se copia el programa original en "programa2", y se resetea "programa" para la generación de nuevo de la tabla de procedimientos
programa2 = programa
programa = Programa()

#Se crea la segunda vuelta del parser
q = yacc.yacc()

q.parse(lexer=lexer2)