print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
#Si se desconoce el número de argumentos de palabras clave, agregue un doble **antes del nombre del parámetro:

def my_function(**kid):
  print("holi como estas " + kid["lname"])

my_function(fname = "alexa", lname = "valeria")