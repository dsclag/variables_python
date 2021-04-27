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

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que determine si una persona_2
es pariente de la persona_1
Para facilitar el ejercicio solo ingresar un nombre
y un apellido por persona
Ingresar dichos datos como Nombre Apellido, es decir,
primero el nombre y luego el apellido, separado por un espacio.
- El programa debe consultar primero el nombre completo de la persona_1
- Luego debe consultar el nombre completo de la persona_2
- Debe extraer el apellido de la persona_2
- Luego preguntar si apellido de la persona_2 está contenido
  en el nombre completo de la persona_1
- En caso de contenerlo, son parientes
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre recomendamos
usar el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca
de este método que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''

print('Comencemos a ponernos serios')
print(" ")
# Empezar aquí la resolución del ejercicio

persona_1 = "Ryan Ray Land Diamond"
persona_2 = "Rihanna Joa Diamond Oconner"
persona_3 = "Bryan Oconner"

nombre, nombre1, apellido, apellido1 = persona_1.split(" ")
[ nombre2, nombre3, apellido2, apellido3] = persona_2.split(" ")
nombre4, apellido4 = persona_3.split(" ")

print("¿Cual es el nombre completo de la persona 1?")
print("El nombre de la persona 1 es: ")
print(persona_1)
print(" ")
print("¿Cual es el nombre completo de la persona 2?")
print("El nombre de la persona 2 es: ")
print(persona_2)
print(" ")
print("¿Cual es el nombre completo de la persona 3?")
print("El nombre de la persona 3 es: ")
print(persona_3)
print(" ")
print(apellido, apellido1)
print(apellido2, apellido3)
print(apellido4)
print(" ")
print("Recolectando datos, espere por favor...")
print(" ")
print(" ")
print(" ")
print(" ")
if apellido in persona_2:
  print("Land esta en el nombre de Rihanna")
else:
  print("Land no esta en el nombre de Rihanna")
print(" ")
if apellido1 in persona_2:
  print("Diamond esta en el nombre de Rihanna")
else:
  print("Diamond no esta en el nombre de Rihanna")
print(" ")
if apellido in persona_3:
  print("Land esta en el nombre de Bryan")
else:
  print("Land no esta en el nombre de Bryan")
print(" ")
if apellido1 in persona_3:
  print("Diamond esta en el nombre de Bryan")
else:
  print("Diamond no esta en el nombre de Bryan")
print(" ")


if apellido2 in persona_1:
  print("Diamond esta en el nombre de Ryan")
else:
  print("Diamond no esta en el nombre de Ryan")
print (" ")
if apellido3 in persona_1:
  print("Oconner esta en el nombre de Ryan")
else:
  print("Oconner no esta en el nombre de Ryan")
print(" ")
if apellido2 in persona_3:
  print("Diamond esta en el nombre de Bryan")
else:
  print("Diamond no esta en el nombre de Bryan")
print(" ")
if apellido3 in persona_3:
  print("Oconner esta en el nombre de Bryan")
else:
  print("Oconner no esta en el nombre de Bryan")
print(" ")


if apellido4 in persona_1:
  print("Oconner esta en el nombre de Ryan")
else:
  print("Oconner no esta en el nombre de Ryan")
print(" ")
if apellido4 in persona_2:
  print("Oconner esta en el nombre de Rihanna")
else:
  print("Oconner no esta en el nombre de Rihanna")
print(" ")
print(" ")
print("Estos son los datos que pude entrelazar:")
print(" ")
print(" ")


if apellido in persona_2:
  print("Ryan es pariente de Rihanna")
if apellido1 in persona_2:
  print("Ryan es pariente de Rihanna")
if apellido in persona_3:
  print("Ryan es pariente de Bryan")
if apellido1 in persona_3:
  print("Ryan es pariente de Bryan")
print(" ")
print(" ")

if apellido2 in persona_1:
  print("Rihanna es pariente de Ryan")
if apellido3 in persona_1:
  print("Rihanna es pariente de Ryan")
if apellido2 in persona_3:
  print("Rihanna es pariente de Bryan")
if apellido3 in persona_3:
  print("Rihanna es pariente de Bryan")
print(" ")
print(" ")


if apellido4 in persona_1:
  print("Bryan es pariente de Ryan")
if apellido4 in persona_2:
  print("Bryan es pariente de Rihanna")
print(" ")
print(" ")
print("Pero a su vez:")
print(" ")
if apellido4 in persona_1:
  print("Bryan es pariente de Ryan")
else:
  print("Bryan no es pariente de Ryan")
print(" ")
if apellido1 in persona_3:
  print("Ryan es pariente de Bryan")
else:
  print("Ryan no es pariente de Bryan")
print(" ")
print("Por ende, estos serian los datos terminados: ")
print(" ")
print(" ")

if apellido1 in persona_2:
  print("Ryan es pariente de Rihanna")
if apellido in persona_3:
  print("Ryan es pariente de Bryan")
else: 
  print("Pero no de Bryan")
print(" ")
  
if apellido2 in persona_1:
  print("Rihanna es pariente de Ryan")
if apellido3 in persona_3:
  print("Rihanna es pariente de Bryan")
print(" ")
if apellido4 in persona_2:
  print("Bryan es pariente de Rihanna")
if apellido4 in persona_1: 
  print("Bryan es pariente de Ryan")
else:
  print("Pero no de Ryan")

'''
Despues de hacer el codigo me di cuenta que lo posida hacer muchisimo mas simple usando un 
in intercalado con un or

'''