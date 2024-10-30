print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
#Puede enviar cualquier tipo de datos de argumento a una función (cadena, número, lista, diccionario, etc.)
#  y se tratará como el mismo tipo de datos dentro de la función.
#Por ejemplo, si envía una lista como argumento, seguirá siendo una lista cuando llegue a la función:

def my_function(food):
  for x in food:
    print(x)

fruits = ["manzana", "mango", "kiwi"]

my_function(fruits)