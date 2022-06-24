myStr = "Hello World"

##dir da lista de los comandos que se pueden usar en un tipo de dato
#print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("Hello", "Hola").upper())
print(myStr.count("l")) #Este esta bkn te cuenta el caracter que pongas dentro del string
print(myStr.startswith("Hola")) #Este te dice si un string parte con un caracter o caracteres
print(myStr.split(" ")) #Aca tambien existe el split para crear arrays
print(myStr.find("o")) #Devuelve el primer indice donde se encuentra el caracter
print(len(myStr)) #devuelve length del string
print(myStr.index("l"))  #devuelve el priner imdex donde se encuentra el carater
print(myStr.isnumeric())
print(myStr.isalpha())
print(myStr[3]) #Asi se controlan los index en py(?)

#no es de la clase pero el index tambien funciona con arrays
myArray = ["qdc", "wsx", "sad"]
print(myArray.index("wsx"))

#maneras de concatenar?
print("My name is " + myStr)
print(f"My name is {myStr}") #para poner variables en strings se tiene que poner una f antes - solo desde 3.6
print("My name is {0}".format(myStr)) #asignacion normal de variables en un string

newStr = "Hola {0}"
print(newStr.format(myStr)) 