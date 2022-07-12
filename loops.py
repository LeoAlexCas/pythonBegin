lista_para_loop = ["lista", "para", "loop"]

for item in lista_para_loop:
    print(item)

#como todo bucle se pueden anidar condicionales

for item in lista_para_loop:
    if item == "para":
        print("el nombre es para")
    print(item)


#los bucles se pueden romper
for item in lista_para_loop:
    if item == "para":
        print("el nombre es para, se hara un BREAK")
        break
    print(f"items: {item}")
#existe continue que se salta la ejecucion del bucle pero continua con los demas elementos


#se pueden establecer rangos e imprimirlos
for number in range(1, 10):
    print(number)

#Se pueden recorrer strings
for letra in "string":
    print(letra)

#existen ciclos while
x = 4
while x < 10:
    print(x)
    x = x+1
