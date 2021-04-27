# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que determine cual sería el apellido de una persona
si se ingresaran los dos nombres completos de sus padres.
Dicha persona deberá tener los apellidos de ambos padres

- Primero el programa debe consultar el nombre completo del padre_1
- Luego el programa debe consultar el nombre completo del padre_2
- Luego debe consultar el nombre del hijo/a
- Debe extraer los apellidos de los padres
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres
  y el nombre ingresado de dicha persona
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca de este método
que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''

print('Jugando con texto')
print(" ")
# Empezar aquí la resolución del ejercicio


print("Ingresar nombre del padre: ")
nPadre = str(input())

print("Ingresar apellido del padre: ")
aPadre = str(input())

comPadre = nPadre + " " + aPadre
comPadre.split()
print(" ")
print("El nombre completo ingresado del padre es: ")
print(comPadre)

print(" ")

print("Ingresar nombre de la madre: ")
nMadre = str(input())

print("Ingresar apellido de la madre: ")
aMadre = str(input())

comMadre = nMadre + " " + aMadre
comMadre.split()
print(" ")
print("El nombre completo ingresado de la madre es: ")
print(comMadre)

print(" ")

print("Ingresar solo el nombre del hijo: ")
nHijo = str(input())
print(" ")

print("Los dos apellidos de los padres son: ")
amApellidos = aPadre +" " + "y" + " " + aMadre
amApellidos2 = aPadre + " " + aMadre
amApellidos3 = aMadre + " " + aPadre
print(amApellidos)
print(" ")

print("Por ende, el nombre completo del hijo seria: ")
aHijo = amApellidos2
ahijo2 = amApellidos3
print(nHijo + " " + aHijo)
print(" ")
print("O bien, tambien podria ser")
print(" ")
print(nHijo + " " + ahijo2)

print(" ")
print(" ")

print("O la ecuacion puede ser ya definida desde antes: ")
print(" ")

nombre_padre = "Ryan Ray"
nombre_madre = "Rihanna Diamond"
nombre, apellido = nombre_padre.split(" ")
nombre1, apellido1 = nombre_madre.split (" ")
nombre_hijo = "Lucqs"

print("El nombre y apellido del padre es: ")
print(nombre_padre)
print(" ")
print("El nombre y apellido de la madre es: ")
print(nombre_madre)
print(" ")
print("El nombre del hijo es: ")
print(nombre_hijo)
print(" ")
print("Haciendo la ecuacion pedida, toda la mezcla quedaria")
print(" ")
apellido_hijo = nombre_hijo + " " + apellido + " " + apellido1
print(apellido_hijo)
