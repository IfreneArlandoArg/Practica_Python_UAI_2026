# 1. Condicionales if, elif y else
# 1. Clasificación de temperatura
tmp = float(input("Ingrese la temperatura en grados Celsius: "))
if tmp < 0 :
    print("Temperatura bajo cero.")
elif 0 <= tmp <= 15 :
    print("Temperatura fría.")      
elif 16 <= tmp <= 25 :
    print("Temperatura templada.")
else :
    print("Temperatura cálida.")

# 2. Descuento según tipo de cliente
importe = float(input("Ingrese el importe de la compra: "))
tipo_cliente = input("Ingrese el tipo de cliente (normal, frecuente o premium): ").lower()
if tipo_cliente == "normal" :
    descuento = 0
elif tipo_cliente == "frecuente" :
    descuento = 0.10
elif tipo_cliente == "premium" :
    descuento = 0.20
else :
    print("Tipo de cliente no válido.")
    descuento = 0
importe_final = importe * (1 - descuento)

print(f"El importe final de la compra es: {importe_final}")

# 3. Aprobación de una asignatura
nota = float(input("Ingrese la nota del examen: "))
if nota >= 4:
    asistencia = float(input("Ingrese el porcentaje de asistencia: "))
    if asistencia >= 75:
        print("Asignatura aprobada")
    else:
        print("Desaprobado por asistencia")
else:
    print("Desaprobado por nota")

# 4. Ingreso hasta cero
cantidad = 0
suma = 0
numero = int(input("Ingrese un número entero (0 para finalizar): "))
while numero != 0:
    cantidad += 1
    suma += numero
    numero = int(input("Ingrese otro número entero (0 para finalizar): "))
print(f"Cantidad de números: {cantidad}")
print(f"Suma total: {suma}")

# 5. Validación de contraseña
intentos = 0
contrasena = ""
while contrasena != "python123":
    contrasena = input("Ingrese la contraseña: ")
    intentos += 1
print(f"Contraseña correcta. Intentos necesarios: {intentos}")

# 6. Número secreto
numero_secreto = 27
intento = int(input("Adivine el número secreto: "))
while intento != numero_secreto:
    if intento > numero_secreto:
        print("El número ingresado es mayor")
    else:
        print("El número ingresado es menor")
    intento = int(input("Intente nuevamente: "))
print("¡Adivinaste el número secreto!")

# 7. Recorrer una lista
numeros = [4, 7, 2, 9, 12, 15, 20]
print("Números pares:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)

# 8. Uso de range()
numero = int(input("Ingrese un número entero positivo: "))
for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")

# 9. Acumulación con range()
inicio = int(input("Ingrese el inicio del intervalo: "))
final = int(input("Ingrese el final del intervalo: "))
suma_divisibles = 0
for numero in range(inicio, final + 1):
    if numero % 3 == 0:
        suma_divisibles += numero
print(f"Suma de los divisibles por 3: {suma_divisibles}")

# 10. Cálculo de superficie
def superficie_rectangulo(base, altura):
    return base * altura


base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
print(f"Superficie: {superficie_rectangulo(base, altura)}")

# 11. Determinar el mayor
def mayor_de_tres(numero1, numero2, numero3):
    return max(numero1, numero2, numero3)


print(f"El mayor es: {mayor_de_tres(8, 15, 11)}")

# 12. Contar vocales
def contar_vocales(texto):
    return sum(1 for caracter in texto.lower() if caracter in "aeiouáéíóú")


print(f"Cantidad de vocales: {contar_vocales('Programación en Python')}")

# 13. Aplicar operación
def aplicar_operacion(numero1, numero2, operacion):
    return operacion(numero1, numero2)


print(aplicar_operacion(10, 3, lambda primero, segundo: primero + segundo))
print(aplicar_operacion(10, 3, lambda primero, segundo: primero - segundo))
print(aplicar_operacion(10, 3, lambda primero, segundo: primero * segundo))

# 14. Transformar una lista
def transformar_lista(lista, operacion):
    return [operacion(numero) for numero in lista]


lista = [2, 4, 6, 8]
print(f"Dobles: {transformar_lista(lista, lambda numero: numero * 2)}")
print(f"Cuadrados: {transformar_lista(lista, lambda numero: numero * numero)}")

# 15. Filtrar elementos
def filtrar_elementos(lista, condicion):
    return [numero for numero in lista if condicion(numero)]


lista = [3, 8, 11, 14, 17, 20]
print(f"Pares: {filtrar_elementos(lista, lambda numero: numero % 2 == 0)}")
print(f"Mayores que 10: {filtrar_elementos(lista, lambda numero: numero > 10)}")

# 16. Crear multiplicador
def crear_multiplicador(factor):
    return lambda numero: numero * factor


multiplicar_por_5 = crear_multiplicador(5)
print(f"7 multiplicado por 5: {multiplicar_por_5(7)}")

# 17. Crear calculador de descuento
def crear_calculador_descuento(porcentaje):
    return lambda precio: precio * (1 - porcentaje / 100)


descuento_20 = crear_calculador_descuento(20)
print(f"Precio con 20 % de descuento: {descuento_20(1000)}")

# 18. Crear potencia
def crear_potencia(exponente):
    return lambda numero: numero ** exponente


cuadrado = crear_potencia(2)
cubo = crear_potencia(3)
print(f"Cuadrado de 4: {cuadrado(4)}")
print(f"Cubo de 3: {cubo(3)}")

# 19. Mensajes antes y después
from functools import wraps


def mensajes_antes_y_despues(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        print("Inicio de la función")
        resultado = funcion(*args, **kwargs)
        print("Fin de la función")
        return resultado

    return envoltura


@mensajes_antes_y_despues
def saludar():
    print("Hola")


saludar()

# 20. Convertir resultado a mayúsculas
def convertir_a_mayusculas(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        return funcion(*args, **kwargs).upper()

    return envoltura


@convertir_a_mayusculas
def obtener_mensaje():
    return "mensaje en minúsculas"


print(obtener_mensaje())

# 21. Contador de ejecuciones
def contar_ejecuciones(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        envoltura.cantidad += 1
        return funcion(*args, **kwargs)

    envoltura.cantidad = 0
    return envoltura


@contar_ejecuciones
def mostrar_numero(numero):
    print(f"Número: {numero}")


mostrar_numero(1)
mostrar_numero(2)
mostrar_numero(3)
print(f"La función se ejecutó {mostrar_numero.cantidad} veces")

# 22. Generador de números pares
def generar_pares(n):
    for numero in range(0, n + 1, 2):
        yield numero


print(f"Pares hasta 10: {list(generar_pares(10))}")

# 23. Cuenta regresiva
def cuenta_regresiva(n):
    for numero in range(n, -1, -1):
        yield numero


print(f"Cuenta regresiva: {list(cuenta_regresiva(5))}")

# 24. Generador de múltiplos
def generar_multiplos(valor, cantidad):
    for multiplicador in range(1, cantidad + 1):
        yield valor * multiplicador


print(f"Múltiplos de 5: {list(generar_multiplos(5, 4))}")

# 25. Suma de números naturales
def suma_naturales(n):
    if n <= 0:
        return 0
    return n + suma_naturales(n - 1)


print(f"Suma de los primeros 5 naturales: {suma_naturales(5)}")

# 26. Potencia recursiva
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    if exponente < 0:
        return 1 / potencia_recursiva(base, -exponente)
    return base * potencia_recursiva(base, exponente - 1)


print(f"2 elevado a 4: {potencia_recursiva(2, 4)}")

# 27. Suma de los elementos de una lista
def sumar_lista(lista):
    if not lista:
        return 0
    return lista[0] + sumar_lista(lista[1:])


print(f"Suma de la lista: {sumar_lista([4, 7, 2, 5])}")