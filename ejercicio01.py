
A = int(input("Ingrese el tamaño de los arreglos"))
N = []
L = []
for i in range (0,A):
 N.append(input("Ingrese nombre de las personas"))
print(N)
for j in range (0,A):
 L.append(len(N[j]))
print(L)