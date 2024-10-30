print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
#Si se desconoce el número de argumentos, agregue un *antes del nombre del parámetro:
def my_function(*kids):
  print("hola como estas " + kids[0])

my_function(" alexa ", " valeria ", " maria ")