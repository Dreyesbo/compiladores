import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

tablaclases = []
contclases = 0
contmetodos = 0
punt = 0
puntvars = 0
varsrandom = 0

class Expr: pass

class BinOp(Expr):
    def __init__(self,left,op,right):
        self.type = "binop"
        self.left = left
        self.right = right
        self.op = op

class Ctei(Expr):
    def __init__(self, name, value):
        self.type = "int"
        self.value = value
        self.name = name

    def __init__(self, name):
    	self.type = "int"
    	self.name = name
    	print("Soy un INT y mi nombre es %s" % self.name)

class Ctef(Expr):
    def __init__(self,name, value):
        self.type = "float"
        self.value = value
        self.name = name

    def __init__(self,name):
        self.type = "float"
        self.name = name
        print("Soy un FLOAT y mi nombre es %s" % self.name)

class Ctes(Expr):
    def __init__(self,name, value):
        self.type = "string"
        self.value = value
        self.name = name

    def __init__(self,name):
        self.type = "string"
        self.name = name
        print("Soy un STRING y mi nombre es %s" % self.name)

class Cteb(Expr):
    def __init__(self,name, value):
        self.type = "bool"
        self.value = value
        self.name = name

    def __init__(self,name):
        self.type = "bool"
        self.name = name
        print("Soy un BOOL y mi nombre es %s" % self.name)

def cuboSemantico(exp1,exp2):
	if exp1 == exp2:
		print "Los tipos son usados correctamente"
	else:
		print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Error de tipo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

def p_clase(p):
	'clase : CLASS clase_a a'
	global varsrandom
	if varsrandom == 0:
		print tablaclases
		varsrandom+=1

def p_clase_a(p):
	'clase_a : ID'
	global punt
	global puntvars
	puntvars = 0
	for i in range(len(tablaclases)):
		#print ("for clase %s" % i)
		if p[1] in tablaclases[i][0]:
			print ("Ya existe la clase %s" % p[1])
		else:
			if len(tablaclases) == i +1:
				punt += 1
				#print ("%s" % p[1])
				tablaclases.append([p[1]])
	if len(tablaclases) == 0:
		tablaclases.append([p[1]])
	#print ("Salgo de la clase %s" % p[1])

def p_a(p):
	'''a : EXTENDS ID b
		| b'''

def p_b(p):
	'b : OCURLY programa CCURLY bb'


def p_bb(p):
	'''bb : clase
		| '''

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
	global punt
	global puntvars
	print ("globales ")
	print ("puntglobal %s" % punt)
	tablaclases[punt].append(['globales'])
	puntvars += 1

def p_ddddd(p):
	'ddddd : GLOBAL'
	global punt
	global puntvars
	#print ("globales1 ")


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
	global punt
	global puntvars
	#print ("punt %s" % punt)
	#print ("puntvars %s" % puntvars)

	if p[1] == "int":
		if len(tablaclases[punt][1]) > 1:
			for x in range(len(tablaclases[punt][1][1])):
				if p[2] == tablaclases[punt][1][1][x].name:
					print ("Ya existe la variabe %s" % p[2])
				else:
					#print ("ELSEEEEEssss error en int")
					if len(tablaclases[punt][puntvars]) > 1:
						#print ("fordeli")
						#print ("for %s" % punt)
						#print (tablaclases[punt][1][1])
						#print ("%s" % len(tablaclases[punt][puntvars][1]))
						for y in range(len(tablaclases[punt][puntvars][1])):
							if p[2] == tablaclases[punt][puntvars][1][y].name:
								print ("Ya existe la variable", p[2], "en", tablaclases[punt][puntvars][0])
								break;
							elif x == len(tablaclases[punt][puntvars][1])-1:
								print ("%s" % p[2])
								tablaclases[punt][puntvars][1].append(Ctei(p[2]))
								print ("Meti var %s" % p[2])
					else:
						tablaclases[punt][puntvars].append([Ctei(p[2])])
						print ("Meti var %s" % p[2])
			
		else:
			tablaclases[punt][puntvars].append([Ctei(p[2])])
			print ("Meti var %s" % p[2])
	if p[1] == "float":
		if len(tablaclases[punt][1]) > 1:
			for x in range(len(tablaclases[punt][1][1])):
				if p[2] == tablaclases[punt][1][1][x].name:
					print ("Ya existe la variabe %s" % p[2])
				else:
					print ("ELSEEEEEssss error en float")
					if len(tablaclases[punt][puntvars]) > 1:
						#print ("fordeli")
						#print ("for %s" % punt)
						#print (tablaclases[punt][1][1])
						#print ("%s" % len(tablaclases[punt][puntvars][1]))
						for y in range(len(tablaclases[punt][puntvars][1])):
							if p[2] == tablaclases[punt][puntvars][1][y].name:
								print ("Ya existe la variabe %s" % p[2])
							elif x == len(tablaclases[punt][puntvars][1])-1:
								print ("%s" % p[2])
								tablaclases[punt][puntvars][1].append(Ctef(p[2]))
								print ("Meti var %s" % p[2])
					else:
						tablaclases[punt][puntvars].append([Ctef(p[2])])
						print ("Meti var %s" % p[2])
			
		else:
			tablaclases[punt][puntvars].append([Ctef(p[2])])
			print ("Meti var %s" % p[2])
	if p[1] == "string":
		if len(tablaclases[punt][1]) > 1:
			for x in range(len(tablaclases[punt][1][1])):
				if p[2] == tablaclases[punt][1][1][x].name:
					print ("Ya existe la variabe %s" % p[2])
				else:
					print ("ELSEEEEEssss error en string")
					if len(tablaclases[punt][puntvars]) > 1:
						#print ("fordeli")
						#print ("for %s" % punt)
						#print (tablaclases[punt][1][1])
						#print ("%s" % len(tablaclases[punt][puntvars][1]))
						for y in range(len(tablaclases[punt][puntvars][1])):
							if p[2] == tablaclases[punt][puntvars][1][y].name:
								print ("Ya existe la variabe %s" % p[2])
							elif x == len(tablaclases[punt][puntvars][1])-1:
								print ("%s" % p[2])
								tablaclases[punt][puntvars][1].append(Ctes(p[2]))
								print ("Meti var %s" % p[2])
					else:
						tablaclases[punt][puntvars].append([Ctes(p[2])])
						print ("Meti var %s" % p[2])
			
		else:
			tablaclases[punt][puntvars].append([Ctes(p[2])])
			print ("Meti var %s" % p[2])
	if p[2] == "bool":
		if len(tablaclases[punt][1]) > 1:
			for x in range(len(tablaclases[punt][1][1])):
				if p[2] == tablaclases[punt][1][1][x].name:
					print ("Ya existe la variabe %s" % p[2])
				else:
					print ("ELSEEEEEssss error en bool")
					if len(tablaclases[punt][puntvars]) > 1:
						#print ("fordeli")
						#print ("for %s" % punt)
						#print (tablaclases[punt][1][1])
						#print ("%s" % len(tablaclases[punt][puntvars][1]))
						for y in range(len(tablaclases[punt][puntvars][1])):
							if p[2] == tablaclases[punt][puntvars][1][y].name:
								print ("Ya existe la variabe %s" % p[2])
							elif x == len(tablaclases[punt][puntvars][1])-1:
								print ("%s" % p[2])
								tablaclases[punt][puntvars][1].append(Cteb(p[2]))
								print ("Meti var %s" % p[2])
					else:
						tablaclases[punt][puntvars].append([Cteb(p[2])])
						print ("Meti var %s" % p[2])
			
		else:
			tablaclases[punt][puntvars].append([Cteb(p[2])])
			print ("Meti var %s" % p[2])
	#print("aaaaaaaaaaaaaaaaaaaaaaaaaaa ESTE ES EL TIPO %s" % p[1])
	#print("aaaaaaaaaaaaaaaaaaaaaaaaaaa Y ESTA ES SU VARIABLE %s" % p[2])


def p_h(p):
	'h : ID i'
	#print ("Salgo de vars")
	p[0] = p[1]


def p_i(p):
	'''i : OBRACKET CTEF CBRACKET j
		| EQUAL varcte j
		| j'''
	if len(p) == 5:
		p[0] = p[4]
	if len(p) == 4:
		p[0] = p[3]
	if len(p) == 2:
		p[0] = p[1]
		

def p_j(p):
	'''j : COMMA h
		| SEMICOLON'''
	if len(p) == 3:
		print ("ESTA ES LA VARIABLE DESPUESA DE LA COMAAAAAAAAAAAAAAA %s" % p[2])
		p[0] = p[2]

def p_tipo(p):
	'''tipo : INT
		| FLOAT
		| BOOL
		| STRING'''
	p[0] = p[1]

def p_varcte(p):
	'''varcte : CTEI
		| CTEF
		| CTES
		| FALSE
		| TRUE
		| ID'''
	p[0] = p[1]

def p_metodos(p):
	''' metodos : VOID k
		| tipo k'''

def p_k(p):
	'k : k_k OPARENTHESIS l'


def p_k_k(p):
	'k_k : ID '
	global punt
	global puntvars
	#print ("puntmetodo %s" % punt)
	#print ("puntmetodovar %s" % puntvars)
	for i in range(len(tablaclases[punt])):
		#print ("fordeli")
		#print ("for %s" % punt)
		#print ("for %s" % i)
		#print ("%s" % len(tablaclases[punt]))
		if p[1] in tablaclases[punt][i][0]:
			print ("Ya existe %s el metodo" % p[1])
		else:
			if len(tablaclases[punt]) == i +1:
				print ("%s" % p[1])
				tablaclases[punt].append([p[1]])
				print ("Meti metodo %s" % p[1])
				puntvars += 1
	if len(tablaclases[punt]) == 1:
		tablaclases[punt].append([p[1]])
		print ("Meti metodo %s" % p[1])
		puntvars += 1
	#print ("Salgo de metodo")

def p_l(p):
	'''l : pars ll
		| ll'''

def p_ll(p):
	'll : CPARENTHESIS OCURLY m'

def p_m(p):
	'm : vars mm'

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
	'''asignacion : variable EQUAL expresion SEMICOLON
			| ID asig_a SEMICOLON'''
	#if len(p) == 5:


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
	p[0] = p[1]
	

def p_t(p):
	'''t : OBRACKET CTEF CBRACKET
		| PERIOD ID
		|  '''

def p_expresion(p):
	'expresion : ssexp'
	

def p_ssexp(p):
	'''ssexp : sexp u'''

def p_u(p):
	'''u : OR ssexp
		| AND ssexp
		| '''

def p_sexp(p):
	'sexp : exp v'

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
	'exp : termino x'

def p_x(p):
	'''x : PLUS exp
		| MINUS exp
		| '''

def p_termino(p):
	'termino : factor y'

def p_y(p):
	'''y : MULT termino
		| DIVIDE termino
		| '''

def p_factor(p):
	'factor : z'

def p_z(p):
	'''z : OPARENTHESIS expresion CPARENTHESIS
		| PLUS zz
		| MINUS zz
		| zz'''
	if len(p) == 2:
		p[0] = p[1]
		if p[0] and p[1] is not None:
			print("Estoy mandando", p[0], "y", p[1])
			cuboSemantico(p[0], p[1])
	if len(p) == 3:
		p[0] = p[2]
		if p[0] and p[2] is not None:
			print("Estoy mandando", p[0], "y", p[2], "en la suma o resta")
			cuboSemantico(p[0], p[2])

def p_zz(p):
	'zz : varcte'
	for a in range(len(tablaclases[punt][puntvars])-1):
		if p[1] == tablaclases[punt][puntvars][1][a].name:
			#print("VARCTE VARCTEVARCTEVARCTEVARCTEVARCTEVARCTEVARCTEVARCTEVARCTEVARCTEVARCTEVARCTEVARCTE", p[1], " de tipo ", tablaclases[punt][puntvars][1][a].type)
			p[0] = tablaclases[punt][puntvars][1][a].type

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
	'main : VOID MAIN OPARENTHESIS CPARENTHESIS OCURLY c_c CCURLY'

def p_c_c(p):
	'c_c : cccc ccc'

def p_ccc(p):
	'''ccc : vars ccc
		| d_d'''

def p_cccc(p):
	'cccc : '
	global punt
	global puntvars
	#print ("main ")
	#print ("puntmain %s" % punt)
	tablaclases[punt].append(['MAIN'])
	#print ("Meti metodo MAIN ")
	puntvars += 1

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