#if
x = 21

#no es un bloque de codigo, esta indentado
if x > 20:
    print("x es mayor que 20")
else:
    print("x es 20 o menor")



y = "carlita"
if y == "leo":
    print(f"y es {y}")
elif y == "carlita":
    print(f"y no es leo, es {y}")


#se pueden anidar if obviamente
if y == "carlita":
    if x > 20:
        print("el nombre es carlita y el numero es mayor a 20")

#el operador y es and aca, mas facil de leer
if y == "carlita" and x > 20:
    print("Se cumplieron los 2")

#el operador o es or
if y == "carlita" or y == "leo":
    print(f"Es alguno de los 2 nombres, especificamente {y}")

#la negacion es not
if(not(y == "juan")):
    print("el nombre no es juan")