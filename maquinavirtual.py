listaProcs = []
listaCtes = []
listaCuadruplos = []

with open("codigo.txt") as f:
	data = f.readlines()


	# contLineas = 1
	for line in data:
		listaProcs.append(line.strip().split(','))
	# 	if contLineas == 1:
	# 		listaProcs = line
	# 		contLineas += 1
	# 	elif contLineas == 2:
	# 		listaCtes = line
	# 		contLineas += 1
	# 	elif contLineas == 3:
	# 		listaCuadruplos = line
	# 		contLineas += 1

print listaProcs
# print listaCtes
# print listaCuadruplos