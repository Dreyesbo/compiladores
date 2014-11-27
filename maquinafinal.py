import pickle

listaProcs = []
listaCtes = []
listaCuadruplos = []
pilaRecursiva = []
pilaMetodo = []
memoria = [None]*100000
tempmem = 0
i = 0;
contMemTemp = 70000
pilaNumPars = []
funcion = False
temNumVars = 0
pilaRetornos = []
cuentaEras = 0
tempMem = 0;


obj = open('codigo.txt', 'rb')
programa = pickle.load(obj)
listaProcs = programa[0]
listaCtes = programa[1]
listaCuadruplos = programa[2]
obj.close()

#print(len(listaCuadruplos))

for x in range(len(listaCtes)):
	#print(listaCtes[x][0])
	memoria[int(listaCtes[x][0])] = listaCtes[x][2]
	# print(listaCtes[x][2])

while (i < len(listaCuadruplos)):

	if listaCuadruplos[i][0] == '+':
		if isinstance(listaCuadruplos[i][1], list):
			aux1 = listaCuadruplos[i][1][0]
			aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])

		elif funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
			else:
				aux2 = int(listaCuadruplos[i][2])

			if int(listaCuadruplos[i][3]) >= 70000:
				aux3 = int(memoria[listaCuadruplos[i][3]])
			else: 
				aux3 = int(listaCuadruplos[i][3])
		
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) + int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) + float(aux2)	

		
	elif listaCuadruplos[i][0] == '-':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
				
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) - int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) - float(aux2)		
			
		
	elif listaCuadruplos[i][0] == '++':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
			else:
				aux2 = memoria[listaCuadruplos[i][2]]

			aux3 = memoria[int(listaCuadruplos[i][3])]
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = listaCuadruplos[i][3]

		memoria[int(aux3)] = int(aux1) + int(aux2)	

		

	elif listaCuadruplos[i][0] == '--':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
				
			aux3 = memoria[int(listaCuadruplos[i][3])]
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = listaCuadruplos[i][3]

		memoria[int(aux3)] = int(aux1) - int(aux2)	


	elif listaCuadruplos[i][0] == '*':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
			else:
				aux2 = int(listaCuadruplos[i][2])

			if int(listaCuadruplos[i][3]) >= 70000:
				aux3 = int(memoria[listaCuadruplos[i][3]])
			else: 
				aux3 = int(listaCuadruplos[i][3])
		
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) * int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) * float(aux2)		

			
		

	elif listaCuadruplos[i][0] == '/':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
			else:
				aux2 = int(listaCuadruplos[i][2])

			if int(listaCuadruplos[i][3]) >= 70000:
				aux3 = int(memoria[listaCuadruplos[i][3]])
			else: 
				aux3 = int(listaCuadruplos[i][3])
		
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) / int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) / float(aux2)		

		

	elif listaCuadruplos[i][0] == '=':
		if isinstance(listaCuadruplos[i][3], list):
			aux1 = memoria[listaCuadruplos[i][1]]
			aux3 = memoria[listaCuadruplos[i][3][0]]
			memoria[int(aux3)] = aux1

		elif isinstance(listaCuadruplos[i][1], list):
			aux1 = memoria[listaCuadruplos[i][1][0]]
			aux3 = listaCuadruplos[i][3]
			memoria[int(aux3)] = memoria[int(aux1)]

		elif funcion is True:
			aux1 = memoria[listaCuadruplos[i][1]]
			aux3 = memoria[listaCuadruplos[i][3]]
			if int(aux1) >= 70000:
				if len(pilaRetornos) > 1:
					x = pilaRetornos.pop()
					aux1 = memoria[x]
				else:
					aux1 = memoria[aux1]
					
			memoria[int(aux3)] = aux1
		else:
			aux1 = listaCuadruplos[i][1]
			aux3 = listaCuadruplos[i][3]
			memoria[int(aux3)] = memoria[int(aux1)]
		
	elif listaCuadruplos[i][0] == '>':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]

		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		if aux1 > aux2:
			memoria[int(aux3)] = True
			print
		else: 
			memoria[int(aux3)] = False

		
	elif listaCuadruplos[i][0] == '>=':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]
		
		
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		if aux1 >= aux2:
			memoria[int(aux3)] = True
			print
		else: 
			memoria[int(aux3)] = False

		
	elif listaCuadruplos[i][0] == '<':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]
	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		if aux1 < aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		
	elif listaCuadruplos[i][0] == '<=':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]
	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	

		if aux1 <= aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		
	elif listaCuadruplos[i][0] == '!=': 
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		if aux1 != aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		
	elif listaCuadruplos[i][0] == '==': 
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]
	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		if aux1 == aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		
	elif listaCuadruplos[i][0] == '&&':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		if (aux1 and aux2) == True:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		

	elif listaCuadruplos[i][0] == '||':
		if funcion is True:
			if int(memoria[listaCuadruplos[i][1]]) >= 70000:
				aux1 = memoria[int(memoria[listaCuadruplos[i][1]])]
				tempaux1 = int(listaCuadruplos[i][1])
			else: 
				aux1 = memoria[listaCuadruplos[i][1]]

			if int(memoria[listaCuadruplos[i][2]]) >= 70000:
				aux2 = memoria[int(memoria[listaCuadruplos[i][2]])]
				tempaux2 = int(listaCuadruplos[i][2])
			else:
				aux2 = memoria[listaCuadruplos[i][2]]
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = memoria[listaCuadruplos[i][1]]
			tempaux1 = int(listaCuadruplos[i][1])
			aux2 = memoria[listaCuadruplos[i][2]]
			tempaux2 = int(listaCuadruplos[i][2])
			aux3 = listaCuadruplos[i][3]


	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		if (aux1 or aux2) == True:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		

	#####################################################################

	elif listaCuadruplos[i][0] == 'goto':
		if funcion is True:
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux3 = int(listaCuadruplos[i][3])

		
		i=aux3-1

	elif listaCuadruplos[i][0] == 'gotof':
		if funcion is True:
			aux1 = int(listaCuadruplos[i][1])
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = int(listaCuadruplos[i][1])
			aux3 = int(listaCuadruplos[i][3])

		if memoria[int(aux1)] == False:
			i=aux3-1
			
	
			


	elif listaCuadruplos[i][0] == 'gotov':
		if funcion is True:
			aux1 = int(listaCuadruplos[i][1])
			aux3 = int(listaCuadruplos[i][3])
		else:
			aux1 = int(listaCuadruplos[i][1])
			aux3 = int(listaCuadruplos[i][3])

		if memoria[int(aux1)] == True:
			i=aux3-1
			
		
			

	elif listaCuadruplos[i][0] == 'ERA':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		iniparam=contMemTemp
		numvars = 0 
		funcion = True
		temp =  "\'" + aux1 + "\'"
		for y in range(1, len(listaProcs[int(aux2)+1])):
			if temp == str(listaProcs[int(aux2)+1][y][0]):
				
				for z in range(5, len(listaProcs[int(aux2)+1][y])):
					numvars += 1
				
				break;
		cuentaEras +=1
		pilaNumPars.append(numvars)

				

	elif listaCuadruplos[i][0] == 'param':
		aux1 = listaCuadruplos[i][1] # direccion
		aux2 = listaCuadruplos[i][2] # nada
		aux3 = listaCuadruplos[i][3] # numero de parametro

		if int(memoria[aux1])>=70000:
			memoria[contMemTemp] = memoria[int(memoria[aux1])]
		else:
			memoria[contMemTemp] = memoria[aux1]
		contMemTemp+=1
		

	elif listaCuadruplos[i][0] == 'GOSUB':
		global tempmem
		
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		temp =  "\'" + aux1 + "\'"
		for y in range(1, len(listaProcs[int(aux2)+1])):
			if temp == str(listaProcs[int(aux2)+1][y][0]):
				
				pilaRecursiva.append(i)
				contMemTemp = contMemTemp - int(listaProcs[int(aux2)+1][y][2])
				constanteVars = int(listaProcs[int(aux2)+1][y][3])
				i = int(listaProcs[int(aux2)+1][y][4])-1
				numParam = int(listaProcs[int(aux2)+1][y][2])
				pilaMetodo.append([int(aux2)+1,y, numParam,  numvars])
				for z in range(5, 5+int(numParam)):
					memoria[int(listaProcs[int(aux2)+1][y][z][2])] = contMemTemp
					contMemTemp+=1
				
				for w in range(int(numParam), numvars):
					memoria[int(listaProcs[int(aux2)+1][y][w+5][2])] = contMemTemp
					contMemTemp+=1
					if w == numvars-1:
						pilaRetornos.append(memoria[int(listaProcs[int(aux2)+1][y][w+5][2])])
				tempMem = contMemTemp
				break;

			

	

	elif listaCuadruplos[i][0] == 'retorno':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]

		if funcion is True:
			if int(aux1) < 70000:
				temp = memoria[int(listaProcs[aux3+1][aux2+1][len(listaProcs[aux3+1][aux2+1])-1][2])]
				if int(memoria[aux1]) < 70000:
					memoria[int(temp)] = int(memoria[aux1])
				else:
					if cuentaEras ==1:
						memoria[int(temp)] = int(memoria[aux1])
					else:
						memoria[int(temp)] = memoria[int(memoria[aux1])]
			else:
				temp = memoria[int(memoria[int(listaProcs[aux3+1][aux2+1][len(listaProcs[aux3+1][aux2+1])-1][2])])]
				memoria[int(temp)] = int(memoria[aux1])

				if int(memoria[aux1]) > 70000:
					temp = memoria[int(listaProcs[aux3+1][aux2+1][len(listaProcs[aux3+1][aux2+1])-1][2])]
					memoria[int(temp)] = memoria[int(memoria[aux1])]
				else:
					temp = memoria[int(memoria[int(listaProcs[aux3+1][aux2+1][len(listaProcs[aux3+1][aux2+1])-1][2])])]
					memoria[int(temp)] = int(memoria[aux1])

		else:
			memoria[int(listaProcs[aux3+1][aux2+1][len(listaProcs[aux3+1][aux2+1])-1][2])] = memoria[aux1]

	elif listaCuadruplos[i][0] == 'RET':
		i = pilaRecursiva.pop()
		pars = pilaNumPars.pop()
		if len(pilaNumPars) == 0:
			funcion = False
		if funcion == True:
			tempRet = pilaMetodo.pop()
			for x in range (tempRet[3]-1,-1,-1):
				memoria[int(listaProcs[tempRet[0]][tempRet[1]][5+x][2])] = tempMem - pars -1		
				tempMem-=1
		else:
			if cuentaEras is not 1:
				tempRet = pilaMetodo.pop()
				for x in range (tempRet[3]-1,tempRet[2]-2,-1):
					memoria[int(listaProcs[tempRet[0]][tempRet[1]][5+x][2])] = memoria[int(tempMem-1)]		
					tempMem-=1
			else:
				tempRet = pilaMetodo.pop()
				for x in range (tempRet[3]-1,tempRet[2]-2,-1):
					memoria[int(listaProcs[tempRet[0]][tempRet[1]][5+x][2])] = memoria[int(memoria[int(tempMem-1)])]		
					tempMem-=1
			cuentaEras = 0
			pilaRetornos = []

		




	elif listaCuadruplos[i][0] == 'END':
		i = len(listaCuadruplos)
		print("END: ", i)




	elif listaCuadruplos[i][0] == 'print':
		if isinstance(listaCuadruplos[i][1], list):
			aux1 = memoria[int(listaCuadruplos[i][1][0])]
			aux2 = listaCuadruplos[i][2]
			aux3 = listaCuadruplos[i][3]
		else:
			aux1 = listaCuadruplos[i][1]
			aux2 = listaCuadruplos[i][2]
			aux3 = listaCuadruplos[i][3]
		print("PRINT: ", memoria[int(aux1)], "\n" )
		
	i+=1
