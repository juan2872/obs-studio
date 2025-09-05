# modelo.py

# Definimos la clase Usuario (representa un dato del sistema)
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Una "base de datos" muy simple: una lista
usuarios = []

# Función para agregar un usuario
def agregar_usuario(nombre, edad):
    usuario = Usuario(nombre, edad)
    usuarios.append(usuario)

# Función para obtener todos los usuarios
def obtener_usuarios():
    return usuarios
