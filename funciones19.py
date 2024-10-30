
#Puede combinar los dos tipos de argumentos en la misma función.
#Cualquier argumento antes de / ,son solo posicionales, y cualquier argumento después de *, son solo palabras clave.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(7, 9, c = 3, d = 9)