#1. Usando map extraer de una lista de listas el primer y último elemento de cada lista
listalistas= [[1,2,3],[4,5,6],[7,8,9]]
primeult = list(map(lambda x: [x[0]]+[x[len(x)-1]],listalistas ))
print(primeult)

#2. Dada una lista de números enteros, usando map y filter retornar 
#una lista con los números superpares (aquellos cuyos todos sus dígitos 

#3. Usando reduce y map extraer los valores máximos de cada lista de una lista de listas 

#4.Usando reduce, map y filter extraer los valores mínimos de cada lista de una lista de 
#listas que cumplen el concepto de número superpar 


#5. Usando map y filter retornar de una lista los valores menores a la potencia 5 de la cabeza de la lista 


#6. Usando map, filter y/o reduce dada una lista de tuplas caracterizada por (int x, int y) sumar los x que
#cumplan con el criterio de ser el número triangular de y 
