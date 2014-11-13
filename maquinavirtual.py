import pickle

listaProcs = []
listaCtes = []
listaCuadruplos = []


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