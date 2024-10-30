print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
#uede especificar que una función puede tener SÓLO argumentos posicionales o SÓLO argumentos de palabras clave.
#Para especificar que una función solo puede tener argumentos posicionales, agregue , / después de los argumentos:

def my_function(x, /):
  print(x)

my_function(6)