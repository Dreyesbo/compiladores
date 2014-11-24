import pickle

listaProcs = []
listaCtes = []
listaCuadruplos = []
pilaRecursiva = []
memoria = [None]*100000
tempmem = 0
i = 0;
contMemTemp = 70000


obj = open('codigo.txt', 'rb')
programa = pickle.load(obj)
listaProcs = programa[0]
listaCtes = programa[1]
listaCuadruplos = programa[2]
paraTemp = []
print (listaProcs)
print ("\n")
print (listaCtes)
print ("\n")
print (listaCuadruplos)
print ("\n")
obj.close()

#print(len(listaCuadruplos))

for x in range(len(listaCtes)):
	#print(listaCtes[x][0])
	memoria[int(listaCtes[x][0])] = listaCtes[x][2]
	# print(listaCtes[x][2])

while (i < len(listaCuadruplos)):
	print ("Cuadruplo: ", i , "  ", listaCuadruplos[i])

	if listaCuadruplos[i][0] == '+':
		aux1 = memoria[listaCuadruplos[i][1]]
		aux2 = memoria[listaCuadruplos[i][2]]
		aux3 = listaCuadruplos[i][3]

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) + int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) + float(aux2)	

		print("Imprime resultado de suma: " , aux1, " + ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '-':
		aux1 = memoria[listaCuadruplos[i][1]]
		aux2 = memoria[listaCuadruplos[i][2]]
		aux3 = listaCuadruplos[i][3]

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) - int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) - float(aux2)		
			
		print("Imprime resultado de resta: " , aux1, " - ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '++':
		aux1 = memoria[listaCuadruplos[i][1]]
		aux2 = memoria[listaCuadruplos[i][2]]
		aux3 = listaCuadruplos[i][3]

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) + int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) + float(aux2)		

		print("Imprime resultado de MASMAS: " , aux1, " ++ ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	
	

	elif listaCuadruplos[i][0] == '--':
		aux1 = memoria[listaCuadruplos[i][1]]
		aux2 = memoria[listaCuadruplos[i][2]]
		aux3 = listaCuadruplos[i][3]

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) - int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) - float(aux2)	

		print("Imprime resultado de MENOSMENOS: " , aux1, " -- ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	


	elif listaCuadruplos[i][0] == '*':
		aux1 = memoria[listaCuadruplos[i][1]]
		aux2 = memoria[listaCuadruplos[i][2]]
		aux3 = listaCuadruplos[i][3]
		

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) * int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) * float(aux2)		

			
		print("Imprime resultado de MULT: " , aux1, " * ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	


	elif listaCuadruplos[i][0] == '/':
		aux1 = memoria[listaCuadruplos[i][1]]
		aux2 = memoria[listaCuadruplos[i][2]]
		aux3 = listaCuadruplos[i][3]


		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) / int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) / float(aux2)		

		print("Imprime resultado de DIV: " , aux1, " / ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	
	

	elif listaCuadruplos[i][0] == '=':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]

		memoria[int(aux3)] = memoria[int(aux1)]

		print("Imprime resultado de asignacion: " , memoria[int(aux1)], " asigna en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '>':
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

		print("Imprime resultado de > : " , aux1, " > ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '>=':
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

		print("Imprime resultado de >= : " , aux1, " >= ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )		

	elif listaCuadruplos[i][0] == '<':
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

		print("Imprime resultado de < : " , aux1, " < ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '<=':
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

		print("Imprime resultado de <= : " , aux1, " <= ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '!=': 
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

		print("Imprime resultado de != : " , aux1, " != ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '==': 
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

		print("Imprime resultado de == : " , aux1, " == ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	

	elif listaCuadruplos[i][0] == '&&':
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

		print("Imprime resultado de && : " , aux1, " && ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )	


	elif listaCuadruplos[i][0] == '||':
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

		print("Imprime resultado de || : " , aux1, " || ", aux2, " = ", memoria[int(aux3)], " en DIR ", aux3, "\n" )		


	#####################################################################

	elif listaCuadruplos[i][0] == 'goto':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = int(listaCuadruplos[i][3])
		print("Cambie el pointer GOTO a: ", aux3, "\n" )
		i=aux3-1

	elif listaCuadruplos[i][0] == 'gotof':
		aux3 = int(listaCuadruplos[i][3])
		aux1 = int(listaCuadruplos[i][1])
		if memoria[int(aux1)] == False:
			i=aux3-1
			print("Checo GOTOF: ", memoria[int(aux1)],  "DIR", aux1)
			print("Cambie el pointer GOTOF a: ", aux3, "\n" )
		else:
			print("Checo GOTOF: ", memoria[int(aux1)],  "DIR", aux1,"\n")


	elif listaCuadruplos[i][0] == 'gotov':
		aux3 = int(listaCuadruplos[i][3])
		aux1 = int(listaCuadruplos[i][1])
		if memoria[int(aux1)] == True:
			i=aux3-1
			print("Checo GOTOV: ", memoria[int(aux1)],  "DIR", aux1)
			print("Cambie el pointer GOTOV a: ", aux3, "\n" )
		else:
			print("Checo GOTOV: ", memoria[int(aux1)],  "DIR", aux1, "\n")

	elif listaCuadruplos[i][0] == 'ERA':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		numvars = 0 
		temp =  "\'" + aux1 + "\'"
		for y in range(1, len(listaProcs[int(aux2)+1])):
			if temp == str(listaProcs[int(aux2)+1][y][0]):
				print("ERA a: ", listaProcs[int(aux2)+1][y][0] )
				for z in range(5, len(listaProcs[int(aux2)+1][y])):
					numvars += 1
					print(listaProcs[int(aux2)+1][y][z])
				print("Numero de variables:",numvars,"\n")	
				break;
				

	elif listaCuadruplos[i][0] == 'param':
		aux1 = listaCuadruplos[i][1] # direccion
		aux2 = listaCuadruplos[i][2] # nada
		aux3 = listaCuadruplos[i][3] # numero de parametro
		paraTemp.append(aux1)
		print ("Lista params: ", paraTemp,"\n")

	elif listaCuadruplos[i][0] == 'GOSUB':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		temp =  "\'" + aux1 + "\'"
		for y in range(1, len(listaProcs[int(aux2)+1])):
			if temp == str(listaProcs[int(aux2)+1][y][0]):
				print("GOSUB a: ", listaProcs[int(aux2)+1][y][0] )
				pilaRecursiva.append(i)
				constanteVars = int(listaProcs[int(aux2)+1][y][3])
				i = int(listaProcs[int(aux2)+1][y][4])-1
				numParam = listaProcs[int(aux2)+1][y][2]
				for z in range(5, 5+int(numParam)):
					memoria[contMemTemp] = memoria[paraTemp.pop()]
					print(listaProcs[int(aux2)+1][y][z][2])
					print(memoria[contMemTemp])
					memoria[int(listaProcs[int(aux2)+1][y][z][2])] = memoria[contMemTemp]
					print("POSICION    :", contMemTemp, "MEMORIA        : ", memoria[contMemTemp], )
					print(memoria[int(listaProcs[int(aux2)+1][y][z][2])])
					contMemTemp+=1
				break;
		print("LAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
		print(constanteVars)
		print(pilaRecursiva)
		print(paraTemp)
		print("\n")

	elif listaCuadruplos[i][0] == 'retorno':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		memoria[int(listaProcs[aux3+1][aux2+1][len(listaProcs[aux3+1][aux2+1])-1][2])] = memoria[aux1]
		print("Retorno: ",memoria[aux1], "en DIR ", aux1, " Metodo: ", aux2, " Clase: ", aux3, "\n")
	

	elif listaCuadruplos[i][0] == 'RET':
		i = pilaRecursiva.pop()
		print("Regresa pointer cuadruplo de llamada: ", i+1, "\n")

	elif listaCuadruplos[i][0] == 'END':
		i = len(listaCuadruplos)
		print("END: ", i)




	elif listaCuadruplos[i][0] == 'print':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		print("PRINT: ", memoria[aux1], "\n" )
		
	i+=1
