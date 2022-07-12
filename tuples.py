#Determinan conjuntos de datos que no pueden ser modificados
newTuple = (1, 2, 3)

print(newTuple)
print(type(newTuple))

#Se pueden asignar con un constructor tambien
x = tuple((1, 2, 3))

#si una tupla tiene un solo elemento y no esta seguido de una coma py asume que es solo un elemento
y = (1)
print(type(y)) #esto es int

j = (1,)
print(type(j)) #esto es tupla

#se pueden borrar tuplas con del
del j
print(j)

#Una llave de diccionario puede ser una tupla
locs = {
    (1, 2): "tupla1"
}