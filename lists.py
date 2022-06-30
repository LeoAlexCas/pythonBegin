from re import T
from xxlimited import new


newList = [1, "a", 4, "b", 1]
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
#si en la lista se repite el elemento, solo tomara el primer index
print(newList.index(1))

#esto es un push al array
rangos.append(10)
print(rangos)

#esto es un push que acepta tuplas y arrays, si se hace con append agregaria el array a los elementos
rangos.extend([11, 12])
print(rangos)

#existe un metodo para insertar elementos en medio de un array
rangos.insert(1, "insertado")
print(rangos)

#hay un pop para sacar elementos del final de la lista o uno que se de en el index
rangos.pop()
print(rangos)

#existe una funcion remove para eliminar elementos especificos
rangos.remove(11)
print(rangos)

#ojo que solo elimina el primer elemento que tiene el valor indicado en el array, no todos
print(newList)
newList.remove(1)
print(newList)

#el metodo clear limpia el array
newList.clear()
print(newList)

#sort aca tambien ordena, pero ademas el sentido del orden se puede definir
rangos.remove("insertado")
rangos.sort()
print(rangos)

rangos.sort(reverse=True)
print(rangos)