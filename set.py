#los sets son listas desordenadas que no tienen indice
newSet = {"set1", "set2", "set3"}

#no se pueden buscar con indices los elementos de un set
print("set1" in newSet)

#se aplican metodos para las listas per no funcionan de igual manera
newSet.add("set6")
print(newSet)

newSet.remove("set1")
print(newSet)

newSet.clear()
print(newSet)