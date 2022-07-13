#python tiene modulos integrados que se deben llamar que cumplen funciones
#Aqui hay un index de los modulos https://docs.python.org/3/py-modindex.html
#Aqui hay modulos de terceros https://pypi.org/ 

#asi se importan
import datetime

#se pueden llamar metodos especficos
from datetime import timedelta

#se usan normal, llamando a la libreria y sacando los metodos
print(datetime.date.today())
print(datetime.datetime.now())

#Llamando a un metodo especifico
print(timedelta(minutes=80))