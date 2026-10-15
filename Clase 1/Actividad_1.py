# Listas

# 1. Promedio de edades
# Solicitar al usuario tres edades, convertir los valores ingresados a int y
# almacenarlos en una lista. Calcular y mostrar el promedio de las edades. Indicar
# además si el promedio es mayor o igual a 18.

edades = []

print("Ingrese tres edades...\n")

i = 0
while i < 3 :
    edad = int(input(f"Ingrese edad {i + 1}: "))
    print(f"Edad ingresada: {edad}")
    edades.append(edad)
    i+=1
    
promedio = sum(edades) / len(edades)
print(f"\nEl promedio de edades es: {promedio}\n")

print("El promedio es igual a 18" if promedio == 18 else "El promedio es mayor a 18" if promedio > 18 else "El promedio es menor a 18")

# 2. Precios de productos
# Crear una lista con cuatro precios de tipo float. Solicitar al usuario una cantidad
# entera y calcular el precio total de cada producto multiplicándolo por dicha
# cantidad. Mostrar únicamente los totales que sean mayores a $10.000.
Precios = [1000.50, 2500.75, 5000.00, 15000.25]

cantidad = int(input("Ingrese la cantidad de productos: "))

Precios_totales = []

for precio in Precios :
    precio_total = precio * cantidad
    Precios_totales.append(precio_total)
    if precio_total > 10000 :
        print(f"El precio total del producto es: ${precio_total}")

# 3. Datos combinados
# Crear una lista que contenga un nombre (str), una edad (int) y una altura (float).
# Mostrar una oración utilizando esos datos y determinar mediante operadores
# lógicos si la persona es mayor de edad y mide más de 1,70 m.

Lista_datos = ["Juan", 25, 1.75]

print(f"\nHola, mi nombre es {Lista_datos[0]}, tengo {Lista_datos[1]} años y mido {Lista_datos[2]} metros.")

if Lista_datos[1] >= 18 and Lista_datos[2] > 1.70 :
    print("La persona es mayor de edad y mide más de 1,70 m.")


# Tuplas

# 4. Coordenadas de un punto
# Solicitar dos números al usuario, convertirlos a float y almacenarlos en una tupla
# que represente las coordenadas (x, y). Calcular la suma y el producto de ambas
# coordenadas.

coordenadas = ()

i = 0
while i < 2 :
    coordenada = float(input(f"Ingrese la coordenada {i + 1}: "))
    coordenadas += (coordenada,)
    print(f"Coordenadas ingresadas: {coordenadas}")
    i+=1
    
suma = sum(coordenadas)
producto = coordenadas[0] * coordenadas[1]

print(f"\nLa suma de las coordenadas es: {suma}")
print(f"El producto de las coordenadas es: {producto}")

# 5. Datos de un producto
# Crear una tupla que contenga el nombre de un producto, su precio y la cantidad
# disponible. Calcular el valor total del stock (precio × cantidad) y determinar si la
# cantidad es mayor que 0 y el valor total supera los $50.000.

Datos_producto = ("Laptop", 1500.00, 40)

Valor_total = Datos_producto[1] * Datos_producto[2]

if Datos_producto[2] > 0 and Valor_total > 50000 :
    print(f"\nEl valor total del stock es: ${Valor_total}")
    print("La cantidad es mayor que 0 y el valor total supera los $50.000.")

# 6. Temperaturas
# Crear una tupla con cinco temperaturas expresadas como números enteros.
# Calcular la temperatura máxima, la mínima y el promedio. Mostrar si el promedio
# se encuentra entre 15 y 25 grados.

temperaturas = (20, 25, 30, 15, 10)

temperatura_maxima = max(temperaturas)
temperatura_minima = min(temperaturas)
promedio_temperatura = sum(temperaturas) / len(temperaturas)

print(f"\nLa temperatura máxima es: {temperatura_maxima}")
print(f"La temperatura mínima es: {temperatura_minima}")
print(f"El promedio de temperatura es: {promedio_temperatura}")

if 15 <= promedio_temperatura <= 25 :
    print("El promedio de temperatura se encuentra entre 15 y 25 grados.")


# Sets

# 7. Números ingresados
# Solicitar al usuario cinco números enteros y almacenarlos en un set. Mostrar
# cuántos valores diferentes fueron ingresados y calcular la suma de todos los
# elementos del conjunto.
numeros = set()

i = 0
while i < 5 :
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.add(numero)
    print(f"Números ingresados: {numeros}")
    i+=1

print(f"Valores diferentes ingresados: {len(numeros)}")
print(f"Suma de los elementos del conjunto: {sum(numeros)}")
    


# 8. Números pares
# Crear un set con varios números enteros. Generar un segundo conjunto que
# contenga solamente aquellos números que sean pares utilizando el operador
# módulo %. Mostrar si el número 10 pertenece al nuevo conjunto.

numeros_enteros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(f"\nNúmeros enteros: {numeros_enteros}")

numeros_pares = {num for num in numeros_enteros if num % 2 == 0}

print(f"\nNúmeros pares: {numeros_pares}")

if 10 in numeros_pares :
    print("\nEl número 10 pertenece al conjunto de números pares.")
else :
    print("\nEl número 10 no pertenece al conjunto de números pares.")

# 9. Materias cursadas
# Crear dos conjuntos con nombres de materias: uno con las materias aprobadas
# y otro con las materias que el alumno está cursando. Mostrar las materias que
# aparecen en ambos conjuntos y determinar si "Programación" pertenece a
# alguno de ellos.
nombre_materias_aprobadas = {"Matemáticas", "Física", "Química", "Programación"}
nombre_materias_cursando = {"Programación", "Biología", "Historia"}

materias_comunes = nombre_materias_aprobadas.intersection(nombre_materias_cursando)

if "Programación" in nombre_materias_aprobadas or "Programación" in nombre_materias_cursando :
    print("\nLa materia 'Programación' pertenece a alguno de los conjuntos.")
else :
    print("\nLa materia 'Programación' no pertenece a ninguno de los conjuntos.")

print(f"\nMaterias comunes: {materias_comunes}")

# Diccionarios

# 10. Datos de un alumno
# Crear un diccionario con las claves "nombre", "edad" y "nota". Solicitar los
# valores al usuario realizando las conversiones necesarias. Mostrar si el alumno
# aprobó considerando que debe tener una nota mayor o igual a 6 y una edad
# mayor o igual a 18.

alumno = {"nombre": input("Ingrese el nombre del alumno: "),
          "edad": int(input("Ingrese la edad del alumno: ")),
          "nota": float(input("Ingrese la nota del alumno: "))}

if alumno["edad"] >= 18 and alumno["nota"] >= 6 :
    print(f"\nEl alumno {alumno['nombre']} aprobó.")
else :
    print(f"\nEl alumno {alumno['nombre']} no aprobó.")

# 11. Compra de un producto
# Crear un diccionario que almacene el nombre de un producto, su precio y la
# cantidad comprada. Calcular el subtotal y, si este supera los $50.000, aplicar un
# descuento del 10 %. Mostrar el importe final.

Producto = {"Nombre": input("Ingrese el nombre del producto: "), 
            "Precio": float(input("Ingrese el precio del producto: ")), 
            "Cantidad": int(input("Ingrese la cantidad comprada: "))}

Subtotal = Producto["Precio"] * Producto["Cantidad"]

if Subtotal > 50000 :
    Descuento = Subtotal * 0.10
    Importe_final = Subtotal - Descuento
    print(f"\nEl subtotal es: ${Subtotal}")
    print(f"Se aplicó un descuento del 10%: ${Descuento}")
    
print(f"El importe final es: ${Importe_final}")
    
# 12. Información de una persona
# Crear un diccionario con nombre, año de nacimiento y altura. Solicitar los valores
# al usuario y convertirlos al tipo de dato correspondiente. Calcular
# aproximadamente la edad de la persona utilizando el año actual y determinar si
# es mayor de edad o mide más de 1,80 m.
from datetime import datetime

Persona = {"Nombre": input("Ingrese el nombre de la persona: "),
           "Año_nacimiento": int(input("Ingrese el año de nacimiento de la persona: ")),
           "Altura": float(input("Ingrese la altura de la persona en metros: "))}

Edad = datetime.now().year - Persona["Año_nacimiento"]

if Edad >= 18 and Persona["Altura"] > 1.80 :
     print(f"\nLa persona {Persona['Nombre']} es mayor de edad y mide más de 1,80 m.")
else :
    print(Persona)
