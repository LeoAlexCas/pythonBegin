print(type(9))
print(type(2.3))

suma = 1 + 10.0
#la suma de un int con un float da float aunque termine en 0
print(type(suma))

#elevar
potencia = 3**2
print(potencia)


#El modulo hace lo mismo que en js
modulo = 3 % 2
print(modulo)

#Este devuelve el resultado solo entero de una div
entero = 3 // 2
print(entero)

#precedencia matematica, se puede modificar con parentesis en las operaciones
pres = 20 - 10 / 5 * 3**2
print(pres)

#El input en python es bastante mas facil que en node
age = input("Insert number: ")
print(f"The number is: {age}")
#Igual lo que llega aca es un string, no podria sumarse, hay que pasaro a int
numberAge = int(age)
print(numberAge + 30)