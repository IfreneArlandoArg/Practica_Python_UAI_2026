# Desarrolle una aplicación para administrar una flota de vehículos. Cree una clase base
# Vehiculo, con patente, modelo, capacidad de combustible y combustible disponible.
# Implemente las clases VehiculoTerrestre, con cantidad de ruedas y consumo por
# kilómetro, y VehiculoAcuatico, con velocidad de navegación y consumo por milla
# náutica. Cree una clase VehiculoAnfibio que herede de ambas.

# El programa deberá:Desarrolle una aplicación para administrar una flota de vehículos. Cree una clase base
# Vehiculo, con patente, modelo, capacidad de combustible y combustible disponible.
# Implemente las clases VehiculoTerrestre, con cantidad de ruedas y consumo por
# kilómetro, y VehiculoAcuatico, con velocidad de navegación y consumo por milla
# náutica. Cree una clase VehiculoAnfibio que herede de ambas.
# El programa deberá:
# • Inicializar correctamente todos los atributos mediante llamadas coopera&vas a
# super().
# • Validar que la capacidad, el consumo y el combus&ble disponible sean valores
# válidos.
# • Implementar un método mostrarCaracteristicas() en todas las clases,
# agregando en cada nivel la información correspondiente.
# • Permi&r que el vehículo anfibio realice recorridos terrestres o acuá&cos.
# • Calcular el combus&ble consumido según el &po y la distancia del recorrido.
# • Lanzar una excepción si no existe combus&ble suficiente para completar el
# viaje.
# • Registrar los viajes realizados y mostrar la distancia total recorrida en cada
# medio.
# • Administrar varios vehículos mediante una lista y un menú de opciones.
# • Mostrar el MRO de VehiculoAnfibio y comprobar que el constructor de
# Vehiculo se ejecuta una sola vez.
# • Inicializar correctamente todos los atributos mediante llamadas coopera&vas a
# super().
# • Validar que la capacidad, el consumo y el combus&ble disponible sean valores
# válidos.
# • Implementar un método mostrarCaracteristicas() en todas las clases,
# agregando en cada nivel la información correspondiente.
# • Permi&r que el vehículo anfibio realice recorridos terrestres o acuá&cos.
# • Calcular el combus&ble consumido según el &po y la distancia del recorrido.
# • Lanzar una excepción si no existe combus&ble suficiente para completar el
# viaje.
# • Registrar los viajes realizados y mostrar la distancia total recorrida en cada
# medio.
# • Administrar varios vehículos mediante una lista y un menú de opciones.
# • Mostrar el MRO de VehiculoAnfibio y comprobar que el constructor de
# Vehiculo se ejecuta una sola vez.


class CombustibleInsuficienteError(Exception):
	pass


class Vehiculo:
	inicializaciones = 0

	def __init__(
		self,
		patente,
		modelo,
		capacidad_combustible,
		combustible_disponible,
		**kwargs,
	):
		if not str(patente).strip():
			raise ValueError("La patente no puede estar vacia.")
		self.patente = patente
		self.modelo = modelo
		self.capacidad_combustible = capacidad_combustible
		self.combustible_disponible = combustible_disponible
		self.viajes = []
		Vehiculo.inicializaciones += 1

	@property
	def capacidad_combustible(self):
		return self._capacidad_combustible

	@capacidad_combustible.setter
	def capacidad_combustible(self, value):
		if value <= 0:
			raise ValueError("La capacidad debe ser mayor que cero.")
		self._capacidad_combustible = value

	@property
	def combustible_disponible(self):
		return self._combustible_disponible

	@combustible_disponible.setter
	def combustible_disponible(self, value):
		if value < 0:
			raise ValueError("El combustible disponible no puede ser negativo.")
		if hasattr(self, "_capacidad_combustible") and value > self.capacidad_combustible:
			raise ValueError("El combustible no puede superar la capacidad.")
		self._combustible_disponible = value

	def mostrarCaracteristicas(self):
		return (
			f"Patente: {self.patente}, Modelo: {self.modelo}, "
			f"Capacidad: {self.capacidad_combustible:.2f} L, "
			f"Combustible disponible: {self.combustible_disponible:.2f} L"
		)

	def _registrar_viaje(self, medio, distancia, consumo):
		if distancia <= 0:
			raise ValueError("La distancia debe ser mayor que cero.")
		combustible_consumido = distancia * consumo
		if combustible_consumido > self.combustible_disponible:
			raise CombustibleInsuficienteError(
				f"Combustible insuficiente: se necesitan {combustible_consumido:.2f} L."
			)
		self.combustible_disponible -= combustible_consumido
		self.viajes.append(
			{
				"medio": medio,
				"distancia": distancia,
				"combustible": combustible_consumido,
			}
		)
		return combustible_consumido

	def distanciaTotal(self, medio):
		return sum(viaje["distancia"] for viaje in self.viajes if viaje["medio"] == medio)


class VehiculoTerrestre(Vehiculo):
	def __init__(self, patente, modelo, capacidad_combustible, combustible_disponible, cantidad_ruedas, consumo_km, **kwargs):
		super().__init__(
			patente,
			modelo,
			capacidad_combustible,
			combustible_disponible,
			**kwargs,
		)
		if cantidad_ruedas <= 0:
			raise ValueError("La cantidad de ruedas debe ser mayor que cero.")
		self.cantidad_ruedas = cantidad_ruedas
		self.consumo_km = self._validar_consumo(consumo_km, "por kilometro")

	@staticmethod
	def _validar_consumo(value, descripcion):
		if value <= 0:
			raise ValueError(f"El consumo {descripcion} debe ser mayor que cero.")
		return value

	def mostrarCaracteristicas(self):
		return (
			f"{super().mostrarCaracteristicas()}, Ruedas: {self.cantidad_ruedas}, "
			f"Consumo terrestre: {self.consumo_km:.2f} L/km"
		)

	def realizarViajeTerrestre(self, distancia):
		return self._registrar_viaje("terrestre", distancia, self.consumo_km)


class VehiculoAcuatico(Vehiculo):
	def __init__(self, patente, modelo, capacidad_combustible, combustible_disponible, velocidad_navegacion, consumo_milla, **kwargs):
		super().__init__(
			patente,
			modelo,
			capacidad_combustible,
			combustible_disponible,
			**kwargs,
		)
		if velocidad_navegacion <= 0:
			raise ValueError("La velocidad de navegacion debe ser mayor que cero.")
		if consumo_milla <= 0:
			raise ValueError("El consumo por milla debe ser mayor que cero.")
		self.velocidad_navegacion = velocidad_navegacion
		self.consumo_milla = consumo_milla

	def mostrarCaracteristicas(self):
		return (
			f"{super().mostrarCaracteristicas()}, Velocidad de navegacion: "
			f"{self.velocidad_navegacion:.2f} nudos, Consumo acuatico: "
			f"{self.consumo_milla:.2f} L/milla nautica"
		)

	def realizarViajeAcuatico(self, distancia):
		return self._registrar_viaje("acuatico", distancia, self.consumo_milla)


class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
	def __init__(
		self,
		patente,
		modelo,
		capacidad_combustible,
		combustible_disponible,
		cantidad_ruedas,
		consumo_km,
		velocidad_navegacion,
		consumo_milla,
	):
		super().__init__(
			patente,
			modelo,
			capacidad_combustible,
			combustible_disponible,
			cantidad_ruedas=cantidad_ruedas,
			consumo_km=consumo_km,
			velocidad_navegacion=velocidad_navegacion,
			consumo_milla=consumo_milla,
		)

	def mostrarCaracteristicas(self):
		return f"{super().mostrarCaracteristicas()}, Tipo: anfibio"

	def realizarViaje(self, medio, distancia):
		if medio.lower() == "terrestre":
			return self.realizarViajeTerrestre(distancia)
		if medio.lower() == "acuatico":
			return self.realizarViajeAcuatico(distancia)
		raise ValueError("El medio debe ser 'terrestre' o 'acuatico'.")


class Flota:
	def __init__(self):
		self.vehiculos = []

	def registrar(self, vehiculo):
		self.vehiculos.append(vehiculo)

	def buscar(self, patente):
		return next((vehiculo for vehiculo in self.vehiculos if vehiculo.patente == patente), None)

	def listar(self):
		for vehiculo in self.vehiculos:
			print(vehiculo.mostrarCaracteristicas())


def mostrarMenu():
	print("\n1. Listar vehiculos")
	print("2. Realizar viaje")
	print("3. Mostrar distancias por medio")
	print("4. Mostrar MRO")
	print("0. Salir")


def ejecutarMenu(flota):
	while True:
		mostrarMenu()
		opcion = input("Seleccione una opcion: ")
		if opcion == "0":
			break
		if opcion == "1":
			flota.listar()
		elif opcion == "2":
			patente = input("Patente: ")
			vehiculo = flota.buscar(patente)
			if vehiculo is None:
				print("No se encontro el vehiculo.")
				continue
			try:
				medio = input("Medio (terrestre/acuatico): ")
				distancia = float(input("Distancia: "))
				combustible = vehiculo.realizarViaje(medio, distancia)
				print(f"Viaje realizado. Combustible consumido: {combustible:.2f} L")
			except (ValueError, CombustibleInsuficienteError) as error:
				print(f"Error: {error}")
		elif opcion == "3":
			patente = input("Patente: ")
			vehiculo = flota.buscar(patente)
			if vehiculo is not None:
				print(f"Distancia terrestre: {vehiculo.distanciaTotal('terrestre'):.2f} km")
				print(f"Distancia acuatica: {vehiculo.distanciaTotal('acuatico'):.2f} millas nauticas")
			else:
				print("No se encontro el vehiculo.")
		elif opcion == "4":
			print([clase.__name__ for clase in VehiculoAnfibio.__mro__])
		else:
			print("Opcion invalida.")



flota = Flota()
inicializaciones_antes = Vehiculo.inicializaciones	
anfibio = VehiculoAnfibio(
		"AA123BB",
		"Explorer",
		100,
		80,
		cantidad_ruedas=4,
		consumo_km=0.5,
		velocidad_navegacion=25,
		consumo_milla=1.2,
)

flota.registrar(anfibio)

print(anfibio.mostrarCaracteristicas())
anfibio.realizarViaje("terrestre", 20)
anfibio.realizarViaje("acuatico", 10)
print(f"Combustible restante: {anfibio.combustible_disponible} L")
print(f"Distancia terrestre: {anfibio.distanciaTotal('terrestre')} km")
print(f"Distancia acuatica: {anfibio.distanciaTotal('acuatico')} millas nauticas")
print(f"Inicializaciones de Vehiculo para este objeto: {Vehiculo.inicializaciones - inicializaciones_antes}")
print("MRO:", [clase.__name__ for clase in VehiculoAnfibio.__mro__])

ejecutarMenu(flota)


