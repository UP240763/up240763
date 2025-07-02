#EXERCICES : DIA 3- NIVEL 1
# 1: Edad
Age = 18          
# 2: Altura
Height = 1.72
# 3: Numero complejo             
NC = 2 + 4j     
# 4:Triangulo          
b = int(input("Ingresa la base del triangulo: "))  #Base de triangulo
h = int(input("Ingresa la altura del triangulo: "))#altura de triangulo
Area = (b*h)/2               #Área del triangulo
print("El Área del triangulo es de: ", Area) 
# 5: Lados de un triangulo
print("\n")
print("|Ingresa los lados del triangulo|")
l1 = int(input("Ingresa el lado a: ")) #Lado 1
l2 = int(input("Ingresa el lado b: ")) #Lado 2
l3= int(input("Ingresa el lado c: "))  #Lado 3
perimetro = l1 + l2 + l3
print("EL perimetro del traingulo es: ", perimetro) #Calcular perimetro

# 6: Área y perimetro de un rectangulo
print("\n")
print("|Área y perimetro de un rectangulo|")
length = int(input("Ingresa la longitud del rectangulo: "))
width = int(input("Ingresa el ancho del rectangulo: "))
a = length * width
perimeter = 2 * (length + width)
print("El área del rectangulo es: ", a , " y el perimetro es: ", perimeter)

# 7: Área y circunferencia de un circulo
print("\n")
print("|Área y Perimetro de un circulo|")
r = int(input("Ingresa el radio del circulo: "))
pi = 3.14
Ac = pi * r ** 2
circumference = 2 * pi * r
print ("El área del circulo es :", Ac) 
print("El perimetro es: ", circumference)

# 8: Pendiente
print("\n")
import math
# Ecuación: y = 2x - 2
m1 = 2
b1 = -2
x_int = (0 - b1) / m1
y_int = b1
print("Pendiente:", m1)
print("Intersección con eje x: (", x_int, ", 0 )")
print("Intersección con eje y: ( 0 ,", y_int, ")")

# 9: Pendiente 2
#Puntos (2,2) y (6,10)
print("\n")
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("\n=== Entre puntos (2,2) y (6,10) ===")
print("Pendiente entre puntos:", m2)
print("Distancia Euclidiana:", distance)

# 10: Comparación
print("\n")
print("¿Las pendientes son iguales?", m1 == m2) 

# 11: Calcular valor
print("\n")
print("|Value|")
for x in range(-10, 5):
    y = x**2 + 6*x + 9
    print(f"{x}\t|\t{y}")
# Verificación de cuándo y es 0
print("\n")
print("Cuando y = 0, el valor de x que satisface la ecuación es:")
x_zero = -3
y_zero = x_zero**2 + 6*x_zero + 9
print(f"x = {x_zero}, y = {y_zero}")


# 12: Longitudes y comparación falsa
print("\n")
print(len("python"))
print(len("dragon"))
print(len("python") != len("dragon"))  # Falsy si son iguales
# 13: operador and
print("'on' en ambos")
print('on' in 'python' and 'on' in 'dragon')
# 14: operador in
print("Verificar si 'jargon' está en la frase")
sentence = "I hope this course is not full of jargon."
print('jargon' in sentence)
# 15: operador on
print("Afirmación falsa: 'on' no está en ambos")
print('on' not in 'python' and 'on' not in 'dragon')
# 16: longitud del texto
print("Convertir longitud a float y luego a string")
le = len("python")
print(float(le))
print(str(le))

# 17: Numeros pares
print("\n")
print("Verificar si un número es par")
num = int(input("Ingresa un número: "))
print(num % 2 == 0)
# 18: Comprobar la división de 7 
print("División de piso")
print(7 // 3 == int(2.7))
# 19: Comprobar el tipo de 10
print("Comparar tipos")
print(type('10') == type(10))
# 20: Comprobar int(9.8)
print("Comparar conversión de '9.8'")
print(int(float('9.8')) == 10)

# 21: Calcular pago por horas
print("\n")
horas = int(input("Horas trabajadas: "))
tarifa = int(input("Tarifa por hora: "))
print("Pago total:", horas * tarifa)
 
# 22: Solicitar años vividos
print("\n")
year = int(input("Ingresa tus años vividos: "))
d = year * 365
h = d * 24
m = h * 60
s = m * 60
print("Has vivido ", s , " segundos.")

# 23: Tabla 
print("\n")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

