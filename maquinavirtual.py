import pickle

listaProcs = []
listaCtes = []
listaCuadruplos = []
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

while (i < len(listaCuadruplos)):
	print (i)
	print (listaCuadruplos[i][0])
	if listaCuadruplos[i][0] == '+':
		print ("entro suma")



	i+=1;
