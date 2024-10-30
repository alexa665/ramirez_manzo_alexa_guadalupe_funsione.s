print(" ")
print("alexa guadalupe ramirez manzo 1205 3-W")
print(" ")
#El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.
#Si llamamos a la función sin argumentos, utiliza el valor predeterminado:

def my_function(country = "francia"):
  print("yo soy de " + country)

my_function("mexico")
my_function("españa")
my_function()
my_function("rusia")
