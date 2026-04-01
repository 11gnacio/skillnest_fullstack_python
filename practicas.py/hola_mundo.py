#Ejercicio 1 saludar

print("Hello World")

print()

# Ejercicio numero 2 concatenar nombres

nombre_uno = (("ignacio"))
print("Hola, " + nombre_uno)

print()

nombre_dos = ("Diaz")
print("Hola", nombre_dos)

print()

# número de la suerte: Ejercicio 3 = contactenar mi numero favorito

numero_suerte = 10
print("Mi nuemero de la suerte es, " + str(numero_suerte))

print()

numero_suerte_dos = 20
print("Mi segundo numero de la suerte es", numero_suerte_dos)

print()

# Ejercicio 4 comida favorita  = imprimir de forma uno y dos

comida1 = "Fideos"
comida2 = "Sopa"
# Forma actual
print(f"Mi comida favorita son los {comida1} y la {comida2}")
#Forma un poco mas antigua
print("Mi comida favorita son los {} y la {}!".format(comida1, comida2))

print()

# Ejercicio 5 xD sorpresa

txt = "hola mundo"

# Combierte todo el texto en Mayusculas
print(txt.upper())

# Combierte todo en minuscula
print(txt.lower())

# Repmplaza un elemento espesifico seleccionando el que quieres cambiar y luego lo cambias
print(txt.replace("mundo", "Ignacio"))
