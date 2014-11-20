import pickle

listaProcs = []
listaCtes = []
listaCuadruplos = []
memoria = [None]*60000
i = 0;


obj = open('codigo.txt', 'rb')
programa = pickle.load(obj)
listaProcs = programa[0]
listaCtes = programa[1]
listaCuadruplos = programa[2]
print (listaProcs)
print ("\n")
print (listaCtes)
print ("\n")
print (listaCuadruplos)
obj.close()

print(len(listaProcs))

for x in range(len(listaCtes)):
	print(listaCtes[x][0])
	memoria[int(listaCtes[x][0])] = listaCtes[x][2]
	print(listaCtes[x][2])


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
			print("Si")
			memoria[int(aux3)] = int(aux1) + int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			print("Si")
			memoria[int(aux3)] = float(aux1) + float(aux2)		

			
		print("Imprime resultado")
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
			print("Si")
			memoria[int(aux3)] = int(aux1) - int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			print("Si")
			memoria[int(aux3)] = float(aux1) - float(aux2)		

			
		print("Imprime resultado")
		print(memoria[int(aux3)])

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
			print("Si")
			memoria[int(aux3)] = int(aux1) * int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			print("Si")
			memoria[int(aux3)] = float(aux1) * float(aux2)		

			
		print("Imprime resultado")
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
			print("Si")
			memoria[int(aux3)] = int(aux1) / int(aux2)	

		if ( aux3 >= 12501  and aux3 <= 15000 ) or (aux3 >= 25001  and aux3 <= 30000) or (aux3 >= 45001 and aux3 <= 50000) :
			print("Si")
			memoria[int(aux3)] = float(aux1) / float(aux2)		

			
		print("Imprime resultado")
		print(memoria[int(aux3)])	

	elif listaCuadruplos[i][0] == '=':
		aux1 = listaCuadruplos[i][1]
		aux2 = listaCuadruplos[i][2]
		aux3 = listaCuadruplos[i][3]

		memoria[int(aux3)] = memoria[int(aux1)]


			
		print("Imprime resultado igual")
		print(memoria[int(aux3)])			
						
	i+=1
