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
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''

print('Sistema de ingreso de datos..')
print(" ")
# Empezar aquí la resolución del ejercicio


naPaciente = "lucas land"
list = "Lucas Ezequiel land"
dni = "41.781.455"
altura = "180cm"
edad = "22 años"
fdn = "27/02/1999"
aler = "Penicilina"

nPaciente1 = "ryan ray"
list1 = "Ryan Reynol Rin"
dni1 = "36.786.941"
altura1 = "177cm"
edad1 = "27 años"
fdn1 = "01/01/1994"

nPaciente2 = "rihanna diamond"
list2 = "Rihanna Diamond"
dni2 = "44.874.264"
altura2 = "168cm"
edad2 = "18 años"
fdn2 = "02/02/2003"

nPaciente3 = "ariana grande"
list3 = "Ariana Grande"
dni3 = "47.529.681"
altura3 = "155cm"
edad3 = "15 años"
fdn3 = "03/03/2006"

print("Posibles pacientes cargados en el sistema de datos: ")
print("")
print("Lucas land")
print("Ryan Ray")
print("Rihanna Diamond")
print("Ariana Grande")
print("")

paciente = input("Introduce el nombre y apellido del paciente: ")
print("")

if naPaciente == paciente.lower():
    print("Estos son los datos que encontre en la base de datos: ")
    print("")
    print("El nombre completo del paciente es: " + list)
    print("El dni del paciente es: " + dni)
    print("La altura del paciente es: " + altura)
    print("La edad del paciente es de:" + edad)
    print("Fecha de nacimiento del paciente: " + fdn)
    print(" ")
    print("Datos adicionales a los solicitados: ")
    print("Alergico a " + aler)

if nPaciente1 == paciente.lower():
    print("Estos son los datos que encontre en la base de datos: ")
    print("")
    print("El nombre completo del paciente es: " + list1)
    print("El dni del paciente es: " + dni1)
    print("La altura del paciente es: " + altura1)
    print("La edad del paciente es de: " + edad1)
    print("Fecha de nacimiento del paciente: " + fdn1)
    print(" ")

if nPaciente2 == paciente.lower():
    print("Estos son los datos que encontre en la base de datos: ")
    print("")
    print("El nombre completo del paciente es: " + list2)
    print("El dni del paciente es: " + dni2)
    print("La altura del paciente es: " + altura2)
    print("La edad del paciente es de:" + edad2)
    print("Fecha de nacimiento del paciente: " + fdn2)
    print(" ")

if nPaciente3 == paciente.lower():
    print("Estos son los datos que encontre en la base de datos: ")
    print("")
    print("El nombre completo del paciente es: " + list3)
    print("El dni del paciente es: " + dni3)
    print("La altura del paciente es: " + altura3)
    print("La edad del paciente es de: " + edad3)
    print("Fecha de nacimiento del paciente: " + fdn3)
    print(" ")

else:
    print("El paciente solicitado no se encuentra en la base de datos")



