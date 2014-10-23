import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

tablaMaestra = []
contclases = 0
contmetodos = 0
punt = 0
puntvars = 0
varsrandom = 0
contCuadruplos = 0

class Expr: pass

class BinOp(Expr):
    def __init__(self,left,op,right):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op

class Programa(Expr):
    def __init__(self):
    	self.name = "Programa"
        self.classes = []

    def __repr__(self, level=0):
	    ret = "\t"*level+repr(self.name)+"\n"
	    for classInstance in self.classes:
	        ret += classInstance.__repr__(level+1)
	    return ret

    def __getitem__(self, level=0):
	    ret = "\t"*level+repr(self.name)+"\n"
	    for classInstance in self.classes:
	        ret += classInstance.__repr__(level+1)
	    return ret

class Clase(Expr):
    def __init__(self, name):
    	for x in range(len(programa.classes)):
    		if programa.classes[x].name == name :
    			print("Ya existe la clase", name)
    			break
    	else:
			self.name = name
			self.methods = [Metodo("void", "global"), Metodo("void", "main")]

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+ "\n"
        for method in self.methods:
            ret += method.__repr__(level+1)
        return ret

    def addMethod(self, methodType, methodName):
		self.methods.append(Metodo(methodType, methodName))

class Metodo(Expr):
    def __init__(self, methodType, name):
    	self.type = methodType
        self.name = name
        self.variables = []

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+"\n"
        for variable in self.variables:
            ret += variable.__repr__(level+1)
        return ret

    def addVariable(self, variableType, name):
		if variableType == "int":
			self.variables.append(Ctei(name))

		if variableType == "float":
			self.variables.append(Ctef(name))

		if variableType == "string":
			self.variables.append(Ctes(name))

		if variableType == "bool":
			self.variables.append(Cteb(name))

class Ctei(Expr):
    def __init__(self, name):
    	self.type = "int"
    	self.name = name

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+ repr(self.type) +"\n"
        return ret

class Ctef(Expr):
    def __init__(self,name):
        self.type = "float"
        self.name = name

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+ repr(self.type) +"\n"
        return ret

class Ctes(Expr):
    def __init__(self,name):
        self.type = "string"
        self.name = name

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+ repr(self.type) +"\n"
        return ret

class Cteb(Expr):
    def __init__(self,name):
        self.type = "bool"
        self.name = name

    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.name)+ repr(self.type) +"\n"
        return ret

def cuboSemantico(exp1,exp2):
	if exp1 == exp2:
		print "Los tipos son usados correctamente"
	else:
		print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Error de tipo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

programa = Programa()
clase = 0
metodo = 0
variable = 0
printnum = 0
POper = []
PilaO = []

def p_clase(p):
	'clase : CLASS clase_a a'
	global printnum
	if printnum == 0:
		print programa[0]
		printnum = printnum +1


def p_clase_a(p):
	'clase_a : ID'
	global clase
	programa.classes.append(Clase(p[1]))

def p_a(p):
	'''a : EXTENDS ID b
		| b'''

def p_b(p):
	'b : OCURLY programa CCURLY bb'

def p_bb(p):
	'''bb : incclase clase
		| '''

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

def p_g(p):
	'g : tipo h'
	global clase
	global metodo
	#print (p[2]," ", clase, " ", metodo )
	programa.classes[clase].methods[metodo].addVariable(p[1], p[2])
	#print("Agrego", p[2], "en la clase [", (clase), "] y metodo [", (metodo), "]")

def p_h(p):
	'h : ID i'
	#print ("Salgo de vars")
	p[0] = p[1]

def p_i(p):
	'''i : OBRACKET CTEI CBRACKET j
		| j'''
	if len(p) == 5:
		p[0] = p[4]
	if len(p) == 2:
		p[0] = p[1]
		

def p_j(p):
	'''j : COMMA h
		| SEMICOLON'''
	if len(p) == 3:
		#print ("ESTA ES LA VARIABLE DESPUESA DE LA COMAAAAAAAAAAAAAAA %s" % p[2])
		p[0] = p[2]

def p_tipo(p):
	'''tipo : INT
		| FLOAT
		| BOOL
		| STRING'''
	p[0] = p[1]

def p_varcte(p):
	'''varcte : CTEI varcte_int
		| CTEF varcte_float
		| CTES varcte_string
		| FALSE varcte_bool
		| TRUE varcte_bool
		| varcte_id'''
	if len(p) == 3:
		p[0] = [p[1], p[2]]
	if len(p) == 2:
		p[0] = p[1]

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

def p_varcte_id(p):
	'''varcte_id : ID'''
	global clase
	global metodo
	for x in range(len(programa.classes[clase].methods[metodo].variables)):
		if programa.classes[clase].methods[metodo].variables[x].name == p[1]:
			p[0] = [programa.classes[clase].methods[metodo].variables[x].name, programa.classes[clase].methods[metodo].variables[x].type]
			break;
		elif x == len(programa.classes[clase].methods[metodo].variables)-1:
			print("No se encontro la variable", p[1], " ", clase, " ", metodo)

def p_metodos(p):
	'''metodos : k'''

def p_k(p):
	'k : k_k OPARENTHESIS l'


def p_k_k(p):
	'''k_k : tipo ID
			| VOID ID'''
	global clase
	global metodo
	tipo = p[1]
	#print("Agrego el metodo", p[2])
	programa.classes[clase].addMethod(p[1], p[2])
	#print("\n Aumento el metodo de", metodo, "a", metodo+1, "\n")
	metodo = metodo + 1

def p_l(p):
	'''l : pars ll
		| ll'''

def p_ll(p):
	'll : CPARENTHESIS OCURLY m'

def p_m(p):
	'm : vars terminavarsmetodo mm'

def p_terminavarsmetodo(p):
	'terminavarsmetodo : '

def p_mm(p):
	'''mm : estatuto n
		| m'''

def p_n(p):
	'''n : return CCURLY 
		| mm'''

def p_return(p):
	'''return : RETURN ssexp SEMICOLON
		| '''

def p_pars(p):
	'pars : tipo ID o'

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
		| ID OPARENTHESIS prefunc
		| READ read
		| PRINT print
		| ID PERIOD llamaobj '''

def p_asignacion(p):
	'''asignacion : variable EQUAL meteequal expresion SEMICOLON
			| ID asig_a SEMICOLON'''
	try:
		if(p[1] is not None and p[4][0]):
			print("=", p[4][0], "", p[1][0])
	except IndexError:
		b = 'sss'

def p_meteequal(p):
	'meteequal : '
	POper.append("=")

def p_asig_a(p):
	'''asig_a : PLUSPLUS
			| MINUSMINUS '''

def p_condicion(p):
	'condicion : OPARENTHESIS ssexp CPARENTHESIS bloque p'

def p_p(p):
	'''p : ELSE pp
		| '''

def p_pp(p):
	'''pp : IF condicion
		| bloque'''

def p_ciclofor(p):
	'ciclofor : OPARENTHESIS parfor CPARENTHESIS bloque'

def p_ciclowhile(p):
	'ciclowhile : OPARENTHESIS ssexp CPARENTHESIS bloque'

def p_prefunc(p):
	'''prefunc : q
			| rrr'''

def p_q(p):
	'q : exp r'

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

def p_variable(p):
	'variable : ID t'
	global clase
	global metodo
	for x in range(len(programa.classes[clase].methods[metodo].variables)):
		if programa.classes[clase].methods[metodo].variables[x].name == p[1]:
			p[0] = [programa.classes[clase].methods[metodo].variables[x].name, programa.classes[clase].methods[metodo].variables[x].type]
			break;
		elif x == len(programa.classes[clase].methods[metodo].variables)-1:
			print("No se encontro la variable", p[1], " ", clase, " ", metodo)
	

def p_t(p):
	'''t : OBRACKET CTEF CBRACKET
		| PERIOD ID
		|  '''

def p_expresion(p):
	'expresion : ssexp'
	p[0] = p[1]

def p_ssexp(p):
	'''ssexp : sexp u'''
	p[0] = p[1]

def p_u(p):
	'''u : OR ssexp
		| AND ssexp
		| '''

def p_sexp(p):
	'sexp : exp v'
	p[0] = p[1]

def p_v(p):
	'''v : MORETHAN w
		| LESSTHAN w
		| NOT w
		| EQUAL w
		| '''

def p_w(p):
	'''w : EQUAL exp
		| exp'''

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
					print(op, opdo1[0], opdo2[0], "temp" + str(contCuadruplos))
					PilaO.append("temp"+ str(contCuadruplos))
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
					print(op, opdo1[0], opdo2[0], "temp" + str(contCuadruplos))
					PilaO.append("temp"+ str(contCuadruplos))
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

def p_zz(p):
	'zz : varcte'
	global clase
	global metodo
	for a in range(len(programa.classes[clase].methods[metodo].variables)):
		#print(programa.classes[clase].methods[metodo].variables[a].name, " ", programa.classes[clase].methods[metodo].variables[a].type)
		if p[1] == programa.classes[clase].methods[metodo].variables[a].name:
			p[0] = [programa.classes[clase].methods[metodo].variables[a].name, programa.classes[clase].methods[metodo].variables[a].type]
			break;
	p[0] = p[1]
	PilaO.append(p[1])

def p_bloque(p):
	'bloque : OCURLY a_a CCURLY'

def p_a_a(p):
	'''a_a : estatuto a_a
		| '''

def p_parfor(p):
	'parfor : asignacion ssexp SEMICOLON ID b_b'

def p_b_b(p):
	'''b_b : PLUSPLUS
		| MINUSMINUS'''

def p_main(p):
	'main : VOID entroamain MAIN OPARENTHESIS CPARENTHESIS OCURLY c_c CCURLY'

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

yacc.yacc()

yacc.parse()