# 1. Clase Persona
# Crear una clase Persona que almacene nombre y edad mediante un constructor.
# Incorporar un método mostrar_datos() que muestre ambos valores y otro método que
# indique si la persona es mayor de edad.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18


# Prueba del ejercicio 1
print("=== Ejercicio 1: Clase Persona ===")
persona1 = Persona("Juan", 25)
persona1.mostrar_datos()
print(f"¿Es mayor de edad? {persona1.es_mayor_de_edad()}")

persona2 = Persona("Ana", 15)
persona2.mostrar_datos()
print(f"¿Es mayor de edad? {persona2.es_mayor_de_edad()}")
print()


# 2. Producto con propiedades
# Crear una clase Producto con los atributos nombre y precio. Implementar precio
# mediante una propiedad con getter y setter, evitando que se puedan asignar valores
# negativos. Incorporar un método que calcule el precio aplicando un porcentaje de
# descuento.

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio if precio >= 0 else 0
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self._precio = valor
        else:
            print("Error: el precio no puede ser negativo")
    
    def calcular_precio_con_descuento(self, porcentaje_descuento):
        descuento = self._precio * (porcentaje_descuento / 100)
        return self._precio - descuento


# Prueba del ejercicio 2
print("=== Ejercicio 2: Producto con propiedades ===")
producto1 = Producto("Laptop", 1000)
print(f"Producto: {producto1.nombre}, Precio: ${producto1.precio}")

producto1.precio = 950
print(f"Nuevo precio: ${producto1.precio}")

precio_con_descuento = producto1.calcular_precio_con_descuento(10)
print(f"Precio con 10% descuento: ${precio_con_descuento}")

producto1.precio = -100
print()


# 3. Cuenta bancaria y encapsulamiento
# Crear una clase CuentaBancaria con titular y un atributo privado __saldo. El saldo
# deberá inicializarse mediante el constructor. Implementar métodos para depositar y
# extraer dinero, evitando retirar un importe superior al saldo disponible. Incorporar una
# propiedad de solo lectura para consultar el saldo.

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial if saldo_inicial >= 0 else 0
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de ${cantidad} realizado. Saldo: ${self.__saldo}")
        else:
            print("Error: la cantidad debe ser positiva")
    
    def extraer(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser positiva")
        elif cantidad > self.__saldo:
            print(f"Error: saldo insuficiente. Saldo disponible: ${self.__saldo}")
        else:
            self.__saldo -= cantidad
            print(f"Extracción de ${cantidad} realizada. Saldo: ${self.__saldo}")


# Prueba del ejercicio 3
print("=== Ejercicio 3: Cuenta Bancaria ===")
cuenta = CuentaBancaria("Carlos", 5000)
print(f"Titular: {cuenta.titular}, Saldo: ${cuenta.saldo}")

cuenta.depositar(1000)
cuenta.extraer(2000)
cuenta.extraer(10000)
print(f"Saldo final: ${cuenta.saldo}")
print()


# 4. Empleado con atributo protegido
# Crear una clase Empleado que contenga nombre y el atributo protegido _sueldo.
# Implementar una propiedad sueldo con getter y setter que impida asignar valores
# menores que cero. Incorporar un método que retorne los datos del empleado.

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self._sueldo = sueldo if sueldo >= 0 else 0
    
    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, valor):
        if valor >= 0:
            self._sueldo = valor
        else:
            print("Error: el sueldo no puede ser negativo")
    
    def obtener_datos(self):
        return f"Empleado: {self.nombre}, Sueldo: ${self._sueldo}"


# Prueba del ejercicio 4
print("=== Ejercicio 4: Empleado con atributo protegido ===")
empleado1 = Empleado("María", 3000)
print(empleado1.obtener_datos())

empleado1.sueldo = 3500
print(f"Nuevo sueldo: ${empleado1.sueldo}")

empleado1.sueldo = -1000
print(empleado1.obtener_datos())
print()


# 5. Método de clase
# Crear una clase Vehiculo con marca, modelo y año. Incorporar un atributo de clase que
# almacene la cantidad total de vehículos creados. Implementar un método de clase
# cantidad_vehiculos() que retorne dicha cantidad.

class Vehiculo:
    cantidad_total = 0
    
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        Vehiculo.cantidad_total += 1
    
    @classmethod
    def cantidad_vehiculos(cls):
        return cls.cantidad_total


# Prueba del ejercicio 5
print("=== Ejercicio 5: Método de clase ===")
vehiculo1 = Vehiculo("Toyota", "Corolla", 2022)
vehiculo2 = Vehiculo("Honda", "Civic", 2023)
vehiculo3 = Vehiculo("Ford", "Mustang", 2021)

print(f"Total de vehículos: {Vehiculo.cantidad_vehiculos()}")
print()

# 6. Constructor alternativo con @classmethod
# Crear una clase Alumno con nombre, apellido y legajo. Incorporar un método de clase
# llamado desde_cadena() que permita crear un objeto a partir de una cadena con el
# siguiente formato:
# "Juan,Pérez,1234"El método deberá separar los datos y retornar una
# nueva instancia de Alumno.

class Alumno:
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
    
    @classmethod
    def desde_cadena(cls, cadena):
        nombre, apellido, legajo = cadena.split(',')
        return cls(nombre, apellido, legajo)
    
    def obtener_datos(self):
        return f"Alumno: {self.nombre} {self.apellido}, Legajo: {self.legajo}"


# Prueba del ejercicio 6
print("=== Ejercicio 6: Constructor alternativo con classmethod ===")
alumno1 = Alumno("Juan", "Pérez", "1234")
print(alumno1.obtener_datos())

alumno2 = Alumno.desde_cadena("María,García,5678")
print(alumno2.obtener_datos())

alumno3 = Alumno.desde_cadena("Carlos,López,9012")
print(alumno3.obtener_datos())
print()

# 7. Herencia de empleados
# Crear una clase base Empleado con nombre y sueldo. Crear las clases derivadas
# EmpleadoAdministrativo y EmpleadoVentas.
# • El administra&vo deberá almacenar además el sector.
# • El vendedor deberá almacenar el porcentaje de comisión.
# Cada clase deberá implementar un método calcular_sueldo() de acuerdo con sus
# características.

class EmpleadoBase:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def calcular_sueldo(self):
        return self.sueldo


class EmpleadoAdministrativo(EmpleadoBase):
    def __init__(self, nombre, sueldo, sector):
        super().__init__(nombre, sueldo)
        self.sector = sector
    
    def calcular_sueldo(self):
        bono = self.sueldo * 0.1
        return self.sueldo + bono


class EmpleadoVentas(EmpleadoBase):
    def __init__(self, nombre, sueldo, porcentaje_comision):
        super().__init__(nombre, sueldo)
        self.porcentaje_comision = porcentaje_comision
    
    def calcular_sueldo(self):
        comision = self.sueldo * (self.porcentaje_comision / 100)
        return self.sueldo + comision


# Prueba del ejercicio 7
print("=== Ejercicio 7: Herencia de empleados ===")
admin = EmpleadoAdministrativo("Ana", 3000, "Recursos Humanos")
print(f"{admin.nombre} (Sector: {admin.sector})")
print(f"Sueldo base: ${admin.sueldo}, Sueldo total: ${admin.calcular_sueldo()}")

vendedor = EmpleadoVentas("Roberto", 2500, 15)
print(f"{vendedor.nombre} (Comisión: {vendedor.porcentaje_comision}%)")
print(f"Sueldo base: ${vendedor.sueldo}, Sueldo total: ${vendedor.calcular_sueldo()}")
print()


# 8. Herencia y sobrescritura de métodos
# Crear una clase Figura que defina un método calcular_area(). Crear las clases
# derivadas Rectangulo, Circulo y Triangulo, cada una con los atributos necesarios y
# sobrescribiendo calcular_area() para obtener el área correspondiente.
# Crear varios objetos y mostrar el área de cada figura.

import math

class Figura:
    def calcular_area(self):
        raise NotImplementedError("Subclase debe implementar este método")


class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def calcular_area(self):
        return self.ancho * self.alto


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2


# Prueba del ejercicio 8
print("=== Ejercicio 8: Herencia y sobrescritura de métodos ===")
rectangulo = Rectangulo(5, 3)
print(f"Área del rectángulo (5 x 3): {rectangulo.calcular_area()}")

circulo = Circulo(4)
print(f"Área del círculo (radio 4): {circulo.calcular_area():.2f}")

triangulo = Triangulo(6, 4)
print(f"Área del triángulo (base 6, altura 4): {triangulo.calcular_area()}")
print()

# 9. Polimorfismo
# A partir de las clases Perro, Gato y Vaca, hacer que todas posean un método
# hacer_sonido() que retorne un sonido diferente.
# Almacenar objetos de las tres clases en una lista y recorrerla invocando:
# animal.hacer_sonido()
# sin preguntar previamente qué tipo de objeto contiene la lista.

class Perro:
    def hacer_sonido(self):
        return "¡Guau!"


class Gato:
    def hacer_sonido(self):
        return "¡Miau!"


class Vaca:
    def hacer_sonido(self):
        return "¡Muuu!"


# Prueba del ejercicio 9
print("=== Ejercicio 9: Polimorfismo ===")
animales = [Perro(), Gato(), Vaca(), Perro(), Gato()]

for animal in animales:
    print(f"{animal.__class__.__name__}: {animal.hacer_sonido()}")
print()


# 10. Sistema de pagos
# Crear una clase base MedioPago con un método procesar_pago(importe).
# Crear las clases derivadas:
# • TarjetaCredito
# • Transferencia
# • BilleteraVirtual
# Cada clase deberá sobrescribir procesar_pago() mostrando un mensaje diferente según
# el medio utilizado.
# Almacenar distintos medios de pago en una lista y procesar el mismo importe utilizando
# polimorfismo.

class MedioPago:
    def procesar_pago(self, importe):
        raise NotImplementedError("Subclase debe implementar este método")


class TarjetaCredito(MedioPago):
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta
    
    def procesar_pago(self, importe):
        return f"Pago de ${importe} procesado con Tarjeta de Crédito ({self.numero_tarjeta[-4:]})"


class Transferencia(MedioPago):
    def __init__(self, banco):
        self.banco = banco
    
    def procesar_pago(self, importe):
        return f"Transferencia de ${importe} realizada a través de {self.banco}"


class BilleteraVirtual(MedioPago):
    def __init__(self, nombre_billetera):
        self.nombre_billetera = nombre_billetera
    
    def procesar_pago(self, importe):
        return f"Pago de ${importe} procesado con {self.nombre_billetera}"


# Prueba del ejercicio 10
print("=== Ejercicio 10: Sistema de pagos ===")
medios_pago = [
    TarjetaCredito("1234567890123456"),
    Transferencia("Banco Central"),
    BilleteraVirtual("PayPal"),
    TarjetaCredito("9876543210987654"),
    BilleteraVirtual("Google Pay")
]

importe_total = 500

for medio in medios_pago:
    print(medio.procesar_pago(importe_total))