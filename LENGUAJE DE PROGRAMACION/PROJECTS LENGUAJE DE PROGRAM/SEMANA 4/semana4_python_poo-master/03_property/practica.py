from datetime import datetime


class Empleada:

    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @property
    def fecha_nacimiento(self):
        anio_actual = datetime.now().year
        return anio_actual - self._edad


# Crear objeto
empleada1 = Empleada("Valeria", "San Martin", 34)

# Mostrar información
print("Nombre:", empleada1._nombre)
print("Apellido:", empleada1._apellido)
print("Edad:", empleada1.edad)
print("Año de nacimiento:", empleada1.fecha_nacimiento)