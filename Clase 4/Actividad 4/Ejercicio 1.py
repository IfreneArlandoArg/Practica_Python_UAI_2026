# 1. Sistema de ges-ón de docentes e inves-gadores
# Desarrolle un sistema para administrar el personal académico de una universidad.
# Implemente una clase base Persona, con DNI, nombre y correo electrónico. A partir de
# ella, cree las clases Docente, que almacene asignaturas y horas semanales, e
# Investigador, que registre proyectos e incentivo por investigación. Finalmente,
# implemente DocenteInvestigador, que herede de ambas.
# El programa deberá:
# • U&lizar constructores coopera&vos con super() para que Persona se inicialice
# una sola vez.
# • Validar mediante propiedades que el DNI no esté vacío y que las horas y los
# importes sean posi&vos.
# • Implementar polimórficamente calcularRemuneracion() y mostrarDatos().
# • Calcular para un docente inves&gador la remuneración docente más el
# incen&vo de inves&gación.
# • Almacenar objetos de los dis&ntos &pos en una lista.
# • Permi&r registrar, buscar por DNI, listar y calcular la remuneración total del
# personal.
# • Evitar el registro de dos personas con el mismo DNI mediante una excepción.
# • Mostrar el MRO de DocenteInvestigador y explicar qué recorrido realiza
# super()

class Persona:
    def __init__(self, dni, nombre, correo):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        if value is None or not str(value).strip():
            raise ValueError("El DNI no puede estar vacío.")
        self._dni = value

    def calcularRemuneracion(self):
        return 0

    def mostrarDatos(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Correo: {self.correo}"
        
class Docente(Persona):
    def __init__(self, dni, nombre, correo, asignaturas, horas_semanales, **kwargs):
        super().__init__(dni, nombre, correo, **kwargs)
        self.asignaturas = asignaturas
        self.horas_semanales = horas_semanales

    @property
    def horas_semanales(self):
        return self._horas_semanales

    @horas_semanales.setter
    def horas_semanales(self, value):
        if value <= 0:
            raise ValueError("Las horas semanales deben ser mayores que cero.")
        self._horas_semanales = value

    def calcularRemuneracion(self):
        return self.horas_semanales * 100

    def mostrarDatos(self):
        return f"{super().mostrarDatos()}, Asignaturas: {self.asignaturas}, Horas semanales: {self.horas_semanales}"
        
class Investigador(Persona):
    def __init__(self, dni, nombre, correo, proyectos, incentivo, **kwargs):
        super().__init__(dni, nombre, correo, **kwargs)
        self.proyectos = proyectos
        self.incentivo = incentivo

    @property
    def incentivo(self):
        return self._incentivo

    @incentivo.setter
    def incentivo(self, value):
        if value <= 0:
            raise ValueError("El incentivo debe ser mayor que cero.")
        self._incentivo = value

    def calcularRemuneracion(self):
        return self.incentivo

    def mostrarDatos(self):
        return f"{super().mostrarDatos()}, Proyectos: {self.proyectos}, Incentivo: {self.incentivo}"
        
class DocenteInvestigador(Docente, Investigador):
    def __init__(self, dni, nombre, correo, asignaturas, horas_semanales, proyectos, incentivo):
        super().__init__(
            dni,
            nombre,
            correo,
            asignaturas,
            horas_semanales,
            proyectos=proyectos,
            incentivo=incentivo,
        )

    def calcularRemuneracion(self):
        return Docente.calcularRemuneracion(self) + self.incentivo

    def mostrarDatos(self):
        return (
            f"{Persona.mostrarDatos(self)}, Asignaturas: {self.asignaturas}, "
            f"Horas semanales: {self.horas_semanales}, Proyectos: {self.proyectos}, "
            f"Incentivo: {self.incentivo}"
        )


class DNIRepetidoError(Exception):
    pass


class PersonalAcademico:
    def __init__(self):
        self.personal = []

    def registrar(self, persona):
        if self.buscarPorDNI(persona.dni) is not None:
            raise DNIRepetidoError(f"Ya existe una persona con DNI {persona.dni}.")
        self.personal.append(persona)

    def buscarPorDNI(self, dni):
        return next((persona for persona in self.personal if persona.dni == dni), None)

    def listar(self):
        for persona in self.personal:
            print(persona.mostrarDatos())

    def calcularRemuneracionTotal(self):
        return sum(persona.calcularRemuneracion() for persona in self.personal)



docente = Docente("30111222", "Ana Perez", "ana@universidad.edu", ["Python", "Bases de datos"], 20)
investigador = Investigador("30444555", "Luis Gomez", "luis@universidad.edu", ["IA aplicada"], 75000)
docente_investigador = DocenteInvestigador( "30888999","Sofia Diaz","sofia@universidad.edu",["Programacion", "IA"], 15,["Sistemas inteligentes"],100000)

personal = PersonalAcademico()
for persona in (docente, investigador, docente_investigador):
    personal.registrar(persona)

print("Personal academico:")
personal.listar()
print(f"\nRemuneracion total: ${personal.calcularRemuneracionTotal()}")
print(f"\nBusqueda por DNI: {personal.buscarPorDNI('30888999').nombre}")
print("\nMRO de DocenteInvestigador:")
print([clase.__name__ for clase in DocenteInvestigador.__mro__])
print("super() sigue el MRO: DocenteInvestigador -> Docente -> Investigador -> Persona.")

try:
    personal.registrar(Docente("30111222", "Otra Persona", "otra@universidad.edu", ["Historia"], 10))
except DNIRepetidoError as error:
    print(f"\nError controlado: {error}")
    

