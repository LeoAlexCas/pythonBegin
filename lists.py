from re import T


newList = [1, "a", 4, "b"]
print(type(newList))

#existe un contructor de listas que es como el new Array de js
number_list = list([1, 2, 3, 4])
#list recive solo un argumento, puede ser un array o una tupla
print(number_list)
print(type(number_list))

#existe una funcion range que genera valores en un rango y eso se puede poner en una lista
rangos = list(range(1, 10))
print(rangos)
print(type(rangos))

#el comando dir permite imprimir una lista
#print(dir(rangos))

print(rangos.index(3))
print(len(rangos))
print(rangos[1])
print(10 in rangos)

#esto es un push al array
rangos.append(10)
print(rangos)

#esto es un push que acepta tuplas y arrays, si se hace con append agregaria el array a los elementos
rangos.extend([11, 12])
print(rangos)