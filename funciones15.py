print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
#Pero al agregarlo, , /obtendrá un error si intenta enviar un argumento de palabra clave:

def my_function(x, /):
  print(x)

my_function(x = 3)