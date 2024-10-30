print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
#Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos:
#  **antes del nombre del parámetro en la definición de la función.
#De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
#Si se desconoce el número de argumentos de palabras clave, agregue un doble **antes del nombre del parámetro:

def my_function(**kid):
  print("mi nombre es " + kid["lname"])

my_function(fname = "guadalupe", lname = "alexa")
