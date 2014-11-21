import pickle

listaProcs = []
listaCtes = []
listaCuadruplos = []
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
obj.close()

#print(len(listaCuadruplos))

for x in range(len(listaCtes)):
	#print(listaCtes[x][0])
	memoria[int(listaCtes[x][0])] = listaCtes[x][2]
	# print(listaCtes[x][2])

while (i < len(listaCuadruplos)):
	print ("Cuadruplo")
	print (i)
	print (listaCuadruplos[i])
	if listaCuadruplos[i][0] == '+':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) + int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) + float(aux2)		

			
		print("Imprime resultado de suma")
		print(memoria[int(aux3)])		

	elif listaCuadruplos[i][0] == '-':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) - int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) - float(aux2)		

			
		print("Imprime resultado de resta")
		print(memoria[int(aux3)])

	elif listaCuadruplos[i][0] == '++':
		print("entre a masmas")
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;
		print(aux1)
		print(aux2)
		print(aux3)
		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) + int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) + float(aux2)			

	elif listaCuadruplos[i][0] == '--':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) - int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) - float(aux2)	

	elif listaCuadruplos[i][0] == '*':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) * int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) * float(aux2)		

			
		print("Imprime resultado de mult")
		print(memoria[int(aux3)])	

	elif listaCuadruplos[i][0] == '/':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;

		if ( aux3 >= 10000  and aux3 <= 12500 ) or (aux3 >= 20001  and aux3 <= 25000) or (aux3 >= 40000 and aux3 <= 45000) :
			memoria[int(aux3)] = int(aux1) / int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			memoria[int(aux3)] = float(aux1) / float(aux2)		

			
		print("Imprime resultado de div")
		print(memoria[int(aux3)])	

	elif listaCuadruplos[i][0] == '=':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]

		memoria[int(aux3)] = memoria[int(aux1)]


		print("Imprime resultado de igual")
		print(memoria[int(aux3)])	

	elif listaCuadruplos[i][0] == '>':
		print("Si entra a comp")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		print(tempaux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		print(tempaux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;

		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if aux1 > aux2:
			memoria[int(aux3)] = True
			print
		else: 
			memoria[int(aux3)] = False

		print("Imprime comparac")
		print(str(memoria[int(aux3)]))

	elif listaCuadruplos[i][0] == '>=':
		print("Si entra a comp")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		print(tempaux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		print(tempaux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]
							break;

		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if aux1 >= aux2:
			memoria[int(aux3)] = True
			print
		else: 
			memoria[int(aux3)] = False

		print("Imprime comparac")
		print(str(memoria[int(aux3)]))		

	elif listaCuadruplos[i][0] == '<':
		print("Si entra a comp")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if aux1 < aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		print("Imprime comparac")
		print(memoria[int(aux3)])

	elif listaCuadruplos[i][0] == '<=':
		print("Si entra a comp")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if aux1 <= aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		print("Imprime comparac")
		print(memoria[int(aux3)])

	elif listaCuadruplos[i][0] == '!=': 
		print("Si entra a comp")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if aux1 != aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		print("Imprime comp not equal")
		print(memoria[int(aux3)])

	elif listaCuadruplos[i][0] == '==': 
		print("Si entra a comp")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if aux1 == aux2:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		print("Imprime comp equal equal")
		print(memoria[int(aux3)])


	elif listaCuadruplos[i][0] == '&&':
		print("Si entra a comp and")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if (aux1 and aux2) == True:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		print("Imprime comp and")
		print(memoria[int(aux3)])


	elif listaCuadruplos[i][0] == '||':
		print("Si entra a comp or")
		aux1 = listaCuadruplos[i][1]
		tempaux1 = int(aux1)
		aux2 = listaCuadruplos[i][2]
		tempaux2 = int(aux2)
		aux3 = listaCuadruplos[i][3]
		if int(aux1) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux1) == int(listaProcs[x][y][z][2]):
							aux1 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux1) > 40000:
			for x in range(len(listaCtes)):
						if int(aux1) == int(listaCtes[x][0]):
							aux1 = memoria[int(listaCtes[x][0])]
							break;
		if int(aux2) <= 40000:
			for x in range(1, len(listaProcs)):
				for y in range(1, len(listaProcs[x])):
					for z in range(5, len(listaProcs[x][y])):
						if int(aux2) == int(listaProcs[x][y][z][2]):
							aux2 = memoria[int(listaProcs[x][y][z][2])]
		elif int(aux2) > 40000:
			for x in range(len(listaCtes)):
						if int(aux2) == int(listaCtes[x][0]):
							aux2 = memoria[int(listaCtes[x][0])]

	
		if (tempaux1 >= 10000  and tempaux1 <= 12500 ) or (tempaux1 >= 20001  and tempaux1 <= 25000) or (tempaux1 >= 40000 and tempaux1 <= 45000) :
			aux1 = int(aux1)

		if (tempaux2 >= 10000  and tempaux2 <= 12500 ) or (tempaux2 >= 20001  and tempaux2 <= 25000) or (tempaux2 >= 40000 and tempaux2 <= 45000):
			aux2 = int(aux2)

		if (tempaux1 >= 12501  and tempaux1 <= 15000 ) or (tempaux1 >= 25001  and tempaux1 <= 30000) or (tempaux1 >= 45001 and tempaux1 <= 50000) :
			aux1 = float(aux1)	

		if (tempaux2 >= 12501  and tempaux2 <= 15000 ) or (tempaux2 >= 25001  and tempaux2 <= 30000) or (tempaux2 >= 45001 and tempaux2 <= 50000) :
			aux2 = float(aux2)	
				
		print(aux1)
		print(aux2)
		if (aux1 or aux2) == True:
			memoria[int(aux3)] = True
		else: 
			memoria[int(aux3)] = False

		print("Imprime comp or")
		print(memoria[int(aux3)])	


	#####################################################################

	elif listaCuadruplos[i][0] == 'goto':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = int(listaCuadruplos[i][3])
		print("entre goto")
		print(aux3)
		i=aux3-1

	elif listaCuadruplos[i][0] == 'gotof':
		print("entre gotof")
		aux3 = int(listaCuadruplos[i][3])
		aux1 = int(listaCuadruplos[i][1])
		print(int(listaCuadruplos[i][1]))
		print(memoria[(listaCuadruplos[i][1])])
		print(aux1)
		if memoria[int(aux1)] == False:
			print("sali gotof")
			i=aux3-1
		print(aux3)
		print(aux1)
	
	elif listaCuadruplos[i][0] == 'ERA':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		numvars = 0 
		temp =  "\'" + aux1 + "\'"
		for y in range(1, len(listaProcs[int(aux2)+1])):
			print(listaProcs[int(aux2)+1][y][0])
			if temp == str(listaProcs[int(aux2)+1][y][0]):
				print("Entocntro num vars")
				for z in range(5, len(listaProcs[int(aux2)+1][y])):
					numvars += 1
					print(listaProcs[int(aux2)+1][y][z])
				print(numvars)	
				break;
				
		print("entre ERA")
		print(str(temp))
	elif listaCuadruplos[i][0] == 'param':
		aux1 = listaCuadruplos[i][1] # direccion
		aux2 = listaCuadruplos[i][2] # nada
		aux3 = listaCuadruplos[i][3] # numero de parametro
		paraTemp.append(aux1)
		print (paraTemp)
	elif listaCuadruplos[i][0] == 'GOSUB':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]
		temp =  "\'" + aux1 + "\'"
		for y in range(1, len(listaProcs[int(aux2)+1])):
			print(listaProcs[int(aux2)+1][y][0])
			if temp == str(listaProcs[int(aux2)+1][y][0]):
				numParam = listaProcs[int(aux2)+1][y][2]
				for z in range(5, 5+int(numParam)):
					memoria[contMemTemp] = memoria[paraTemp.pop()]
					print(listaProcs[int(aux2)+1][y][z][2])
					memoria[int(listaProcs[int(aux2)+1][y][z][2])] = memoria[contMemTemp]
					print("POSICION    :", contMemTemp, "MEMORIA        : ", memoria[contMemTemp], )
					contMemTemp+=1
				break;
	i+=1
