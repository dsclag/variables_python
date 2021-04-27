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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
print(" ")
# Empezar aquí la resolución del ejercicio

print("Ingrese por consola el primer numero deseado")
num_1 = int(input())

print("Ingrese por consola el segundo numero deseado")
num_2 = int(input())

suma = (num_1 + num_2)
resta = (num_1 - num_2)
multiplicacion = (num_1 * num_2)
division = (num_1 / num_2)
potencia = (num_1 ** num_2)

print("El resultado de la suma de los numeros introducidos es: ")
print(suma)

print("El resultado de la resta de los numeros introducidos es: ")
print(resta)

print("El resultado de la multiplicacion de los numeros introducidos es:  ")
print(multiplicacion)

print("El resultado de la division de los numeros introducidos es: ")
print(division)

print("El resultado del exponente de los numeros introducidos es: ")
print(potencia)

print(" ")
print("Muchas gracias por usar nuestra calculadora, que tenga buen dia")
