# Desarrolle un sistema de control de usuarios. Implemente una clase base Usuario, con
# nombre de usuario, contraseña y estado activo. Cree las clases Administrador, que
# pueda gestionar usuarios, y Auditor, que pueda consultar registros de actividad.
# Finalmente, implemente AdministradorAuditor, que combine las capacidades de
# ambas clases.
# El programa deberá:
# • Proteger la contraseña y el estado del usuario mediante encapsulamiento.
# • Validar que el nombre de usuario sea único y que la contraseña cumpla una
# longitud mínima.
# • Implementar obtenerPermisos() en las dis&ntas clases u&lizando llamadas
# coopera&vas a super().
# • Evitar que los permisos heredados aparezcan duplicados.
# • Implementar puedeRealizar(accion) para comprobar si un usuario está
# autorizado.
# • Registrar en una colección cada intento de acceso, indicando usuario, acción,
# fecha y resultado.
# • Permi&r crear usuarios, iniciar sesión, ejecutar acciones y consultar el historial.
# • U&lizar polimorfismo para mostrar la información y los permisos de todos los
# usuarios.
# • Lanzar excepciones ante contraseñas incorrectas, usuarios inac&vos o acciones
# no autorizadas.
# • Mostrar el MRO de AdministradorAuditor y explicar cómo Python resuelve el
# problema del diamante

from datetime import datetime


LONGITUD_MINIMA = 8


class ContrasenaIncorrectaError(Exception):
	pass


class UsuarioInactivoError(Exception):
	pass


class AccionNoAutorizadaError(Exception):
	pass


class Usuario:
	def __init__(self, nombre_usuario, contrasena, activo=True, **kwargs):
		if not str(nombre_usuario).strip():
			raise ValueError("El nombre de usuario no puede estar vacio.")
		self.nombre_usuario = nombre_usuario
		self.contrasena = contrasena
		self.activo = activo

	@property
	def contrasena(self):
		return "********"

	@contrasena.setter
	def contrasena(self, value):
		if not isinstance(value, str) or len(value) < LONGITUD_MINIMA:
			raise ValueError(f"La contrasena debe tener al menos {LONGITUD_MINIMA} caracteres.")
		self.__contrasena = value

	@property
	def activo(self):
		return self.__activo

	@activo.setter
	def activo(self, value):
		if not isinstance(value, bool):
			raise ValueError("El estado activo debe ser booleano.")
		self.__activo = value

	def obtenerPermisos(self):
		return ["iniciar_sesion"]

	def puedeRealizar(self, accion):
		return accion in self.obtenerPermisos()

	def mostrarInformacion(self):
		estado = "activo" if self.activo else "inactivo"
		return f"Usuario: {self.nombre_usuario}, Tipo: {self.__class__.__name__}, Estado: {estado}, Permisos: {', '.join(self.obtenerPermisos())}"

	def _verificarContrasena(self, contrasena):
		if contrasena != self.__contrasena:
			raise ContrasenaIncorrectaError("La contrasena es incorrecta.")


class Administrador(Usuario):
	def obtenerPermisos(self):
		return list(dict.fromkeys(super().obtenerPermisos() + ["crear_usuario", "modificar_usuario"]))


class Auditor(Usuario):
	def obtenerPermisos(self):
		return list(dict.fromkeys(super().obtenerPermisos() + ["consultar_historial"]))


class AdministradorAuditor(Administrador, Auditor):
	def obtenerPermisos(self):
		return list(dict.fromkeys(super().obtenerPermisos() + ["consultar_historial"]))


class SistemaUsuarios:
	def __init__(self):
		self.usuarios = []
		self.historial = []

	def _registrarIntento(self, usuario, accion, resultado):
		self.historial.append({
			"usuario": usuario,
			"accion": accion,
			"fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"resultado": resultado,
		})

	def buscarUsuario(self, nombre_usuario):
		return next((usuario for usuario in self.usuarios if usuario.nombre_usuario == nombre_usuario), None)

	def crearUsuario(self, usuario):
		if self.buscarUsuario(usuario.nombre_usuario) is not None:
			raise ValueError("El nombre de usuario ya existe.")
		self.usuarios.append(usuario)

	def iniciarSesion(self, nombre_usuario, contrasena):
		usuario = self.buscarUsuario(nombre_usuario)
		try:
			if usuario is None:
				raise ValueError("El usuario no existe.")
			if not usuario.activo:
				raise UsuarioInactivoError("El usuario esta inactivo.")
			usuario._verificarContrasena(contrasena)
		except (ValueError, UsuarioInactivoError, ContrasenaIncorrectaError) as error:
			self._registrarIntento(nombre_usuario, "iniciar_sesion", f"rechazado: {error}")
			raise
		self._registrarIntento(nombre_usuario, "iniciar_sesion", "aceptado")
		return usuario

	def ejecutarAccion(self, nombre_usuario, contrasena, accion):
		usuario = self.buscarUsuario(nombre_usuario)
		try:
			if usuario is None:
				raise ValueError("El usuario no existe.")
			if not usuario.activo:
				raise UsuarioInactivoError("El usuario esta inactivo.")
			usuario._verificarContrasena(contrasena)
			if not usuario.puedeRealizar(accion):
				raise AccionNoAutorizadaError(f"{nombre_usuario} no puede realizar '{accion}'.")
		except (ValueError, UsuarioInactivoError, ContrasenaIncorrectaError, AccionNoAutorizadaError) as error:
			self._registrarIntento(nombre_usuario, accion, f"rechazado: {error}")
			raise
		self._registrarIntento(nombre_usuario, accion, "aceptado")
		return True

	def listarUsuarios(self):
		for usuario in self.usuarios:
			print(usuario.mostrarInformacion())

	def mostrarHistorial(self):
		for intento in self.historial:
			print(f"{intento['fecha']} | Usuario: {intento['usuario']} | Accion: {intento['accion']} | Resultado: {intento['resultado']}")


def mostrarMenu():
	print("\n1. Listar usuarios")
	print("2. Iniciar sesion")
	print("3. Ejecutar accion")
	print("4. Mostrar historial")
	print("5. Mostrar MRO")
	print("0. Salir")


def ejecutarMenu(sistema):
	while True:
		mostrarMenu()
		opcion = input("Seleccione una opcion: ")
		if opcion == "0":
			break
		if opcion == "1":
			sistema.listarUsuarios()
		elif opcion == "2":
			nombre = input("Usuario: ")
			try:
				sistema.iniciarSesion(nombre, input("Contrasena: "))
				print("Inicio de sesion correcto.")
			except (ValueError, ContrasenaIncorrectaError, UsuarioInactivoError) as error:
				print(f"Error: {error}")
		elif opcion == "3":
			nombre = input("Usuario: ")
			accion = input("Accion: ")
			try:
				sistema.ejecutarAccion(nombre, input("Contrasena: "), accion)
				print("Accion autorizada.")
			except (ValueError, ContrasenaIncorrectaError, UsuarioInactivoError, AccionNoAutorizadaError) as error:
				print(f"Error: {error}")
		elif opcion == "4":
			sistema.mostrarHistorial()
		elif opcion == "5":
			print([clase.__name__ for clase in AdministradorAuditor.__mro__])
			print("super() recorre el MRO y llega a Usuario una sola vez.")
		else:
			print("Opcion invalida.")


sistema = SistemaUsuarios()
sistema.crearUsuario(Administrador("admin", "admin1234"))
sistema.crearUsuario(Auditor("auditor", "auditor123"))
sistema.crearUsuario(AdministradorAuditor("supervisor", "super1234"))
sistema.crearUsuario(Usuario("invitado", "invitado1"))

print("Usuarios registrados:")
sistema.listarUsuarios()
print("\nMRO de AdministradorAuditor:")
print([clase.__name__ for clase in AdministradorAuditor.__mro__])
print("super() evita inicializar Usuario dos veces al seguir el MRO.")

try:
  sistema.iniciarSesion("admin", "admin1234")
  sistema.ejecutarAccion("admin", "admin1234", "crear_usuario")
  sistema.ejecutarAccion("auditor", "auditor123", "crear_usuario")

except (ContrasenaIncorrectaError, UsuarioInactivoError, AccionNoAutorizadaError) as error:
	print(f"\nError controlado: {error}")

ejecutarMenu(sistema)


