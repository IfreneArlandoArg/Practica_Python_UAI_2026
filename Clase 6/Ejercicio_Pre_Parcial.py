# Ejercicio: Gestión de calificaciones de alumnos

# Desarrollar un programa de consola en Python que permita registrar alumnos y administrar sus calificaciones mediante un menú de opciones.

# Los alumnos se almacenarán en un diccionario, cuya clave será el número de legajo. El valor asociado a cada legajo será otro diccionario con dos entradas:

# datos: una tupla con el apellido y el nombre del alumno.

# notas: una lista con sus calificaciones, inicialmente vacía.

# El programa deberá permitir:

# Registrar un alumno: solicitar legajo, apellido y nombre. Verificar que el legajo no esté registrado y crear su estructura de datos.

# Agregar una calificación: solicitar el legajo y una nota numérica entre 0 y 10, que podrá tener decimales. Comprobar que el alumno exista y agregar la nota a su lista.

# Consultar un alumno: mostrar su legajo, apellido, nombre, todas sus notas y su promedio. Si todavía no tiene notas, mostrar “Sin calificaciones”.

# Listar los alumnos aprobados: mostrar el apellido, nombre y promedio de quienes tengan un promedio mayor o igual a 6. Los alumnos sin calificaciones no deberán incluirse.

# Salir del programa.

# Cada una de las primeras cuatro opciones deberá implementarse mediante una función. Además, se deberán desarrollar estas dos funciones auxiliares:

# calcular_promedio(notas): recibirá una lista no vacía de calificaciones y devolverá su promedio.

# obtener_aprobados(alumnos): recibirá el diccionario de alumnos y devolverá una lista de legajos de los aprobados. La función encargada de mostrarlos deberá utilizar esta lista.

# Las funciones deberán recibir mediante parámetros los datos necesarios, evitando el uso de variables globales. Los promedios se mostrarán con dos decimales y el menú se repetirá hasta que el usuario elija salir.

# Para comprobar el funcionamiento, registrar al menos tres alumnos: uno aprobado, uno desaprobado y otro sin calificaciones.


def calcular_promedio(notas):
    """Devuelve el promedio de una lista de calificaciones no vacía."""
    return sum(notas) / len(notas)


def obtener_aprobados(alumnos):
    """Devuelve una lista con los legajos de los alumnos aprobados."""
    aprobados = []

    for legajo, datos in alumnos.items():
        if datos["notas"]:  # solo alumnos con calificaciones
            if calcular_promedio(datos["notas"]) >= 6:
                aprobados.append(legajo)

    return aprobados


def registrar_alumno(alumnos):
    """Registra un alumno nuevo en el diccionario."""
    legajo = int(input("Ingrese el número de legajo: "))

    if legajo in alumnos:
        print("El legajo ya está registrado.")
        return

    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")

    alumnos[legajo] = {
        "datos": (apellido, nombre),
        "notas": []
    }
    print(f"Alumno {apellido}, {nombre} registrado correctamente.")


def agregar_calificacion(alumnos):
    """Agrega una nota a un alumno existente."""
    legajo = int(input("Ingrese el legajo del alumno: "))

    if legajo not in alumnos:
        print("El legajo no existe.")
        return

    nota = float(input("Ingrese la nota (0 a 10): "))

    if 0 <= nota <= 10:
        alumnos[legajo]["notas"].append(nota)
        print("Calificación agregada correctamente.")
    else:
        print("La nota debe estar entre 0 y 10.")


def consultar_alumno(alumnos):
    """Muestra los datos del alumno y su promedio, si tiene notas."""
    legajo = int(input("Ingrese el legajo del alumno: "))

    if legajo not in alumnos:
        print("El legajo no existe.")
        return

    apellido, nombre = alumnos[legajo]["datos"]
    notas = alumnos[legajo]["notas"]

    print(f"Legajo: {legajo}")
    print(f"Apellido: {apellido}")
    print(f"Nombre: {nombre}")
    print(f"Notas: {notas if notas else 'Sin calificaciones'}")

    if notas:
        print(f"Promedio: {calcular_promedio(notas):.2f}")
    else:
        print("Promedio: Sin calificaciones")


def listar_aprobados(alumnos):
    """Muestra los alumnos aprobados con su apellido, nombre y promedio."""
    legajos_aprobados = obtener_aprobados(alumnos)

    if not legajos_aprobados:
        print("No hay alumnos aprobados.")
        return

    print("Alumnos aprobados:")
    for legajo in legajos_aprobados:
        apellido, nombre = alumnos[legajo]["datos"]
        promedio = calcular_promedio(alumnos[legajo]["notas"])
        print(f"- {apellido}, {nombre} - Promedio: {promedio:.2f}")


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Registrar alumno")
    print("2. Agregar calificación")
    print("3. Consultar alumno")
    print("4. Listar alumnos aprobados")
    print("5. Salir")


#def main():
alumnos = {
101: {"datos": ("García", "Ana"), "notas": [8, 9, 7]},
102: {"datos": ("Pérez", "Luis"), "notas": [4, 5, 3]},
103: {"datos": ("López", "Marta"), "notas": []}
}

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_alumno(alumnos)
    elif opcion == "2":
        agregar_calificacion(alumnos)
    elif opcion == "3":
        consultar_alumno(alumnos)
    elif opcion == "4":
        listar_aprobados(alumnos)
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")


#if __name__ == "__main__":
 #   main()
