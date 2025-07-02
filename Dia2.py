#EJERCICIOS. DIA 2 - NIVEL 1

# 2: COMENTARIO
#'Día 2: 30 días de programación en Python'

# 3: variable de nombre
nombre = "José Alberto"
# 4: variable de apellido
apellido = "Quiroz Macias"
# 5: variable con nombre completo
nombre_completo = nombre + " " + apellido
# 6: variable de país
pais = "México"
# 7: variable de ciudad
ciudad = "Aguascalientes"
# 8: variable de edad
edad = 18
# 9: variable de año
anio = 2025
# 10: is_married
is_married = False
# 11: variable is_true
is_true = True
# 12: variable is_light_on
is_light_on = True
# 13: múltiples variables en una línea
nombre2, apellido2, edad2, pais2, ciudad2 = "José", "Alberto", 18, "México", "Aguascalientes"

#EJERCICIOS: NIVEL 2
# 1: Comprobar variables
print(type(nombre))           # str
print(type(apellido))         # str
print(type(nombre_completo))  # str
print(type(pais))             # str
print(type(ciudad))           # str
print(type(edad))             # int
print(type(anio))             # int
print(type(is_married))       # bool
print(type(is_true))          # bool
print(type(is_light_on))      # bool

# 2: Longitud del primer nombre
first_name = 'José Alberto'
print(len(first_name))
# 3: longitud del primer nombre y apellido
last_name = 'Quiroz Macias'
print(len(first_name) > len(last_name))
# 4: Declarar numeros
num_one = 5
num_two = 4
# 5: Suma
total = num_one + num_two
# 6: Resta
diff = num_one - num_two
# 7: Multiplicación
product = num_one * num_two
# 8: División
division = num_one / num_two
# 9: Módulo
remainder = num_two % num_one
# 10: Elevado
exp = num_one ** num_two
# 11: División del piso
floor_division = num_one // num_two
print("Total:", total)
print("Diferencia:", diff)
print("Producto:", product)
print("División:", division)
print("Resto:", remainder)
print("Exponencial:", exp)
print("División entera:", floor_division)
#Circulo
# 12. área
pi = 3.14159
radius = 30

area_of_circle = pi * radius ** 2
# 12.1 : Circunferencia
circum_of_circle = 2 * pi * radius
print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# 12.3. Radio desde input
user_radius = float(input("Ingresa el radio del círculo: "))
user_area = pi * user_radius ** 2
print("Área del círculo con radio del usuario:", user_area)

# 13. Obtener datos del usuario
first_name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
country = input("Ingresa tu país: ")
age = int(input("Ingresa tu edad: "))

print("Nombre completo:", first_name + " " + last_name)
print("País:", country)
print("Edad:", age)