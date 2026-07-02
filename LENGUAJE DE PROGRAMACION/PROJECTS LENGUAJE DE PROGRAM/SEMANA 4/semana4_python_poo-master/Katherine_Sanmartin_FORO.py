"""
Estudiante: Valeria SanMartín
Fecha: 02/07/2026
Asignatura: Lenguaje de Programación Python_FORO

Propósito:
Funciones y clases de python

"""
# ============================================
# FUNCIÓN PARA VALIDAR UNA DIRECCIÓN IP
# ============================================

def validar_ip(ip):

    # Separamos la IP usando el punto
    partes = ip.split(".")

    # Debe tener exactamente 4 partes
    if len(partes) != 4:
        return False

    # Revisamos cada parte
    for parte in partes:

        # Verificamos que sean números
        if not parte.isdigit():
            return False

        numero = int(parte)

        # Debe estar entre 0 y 255
        if numero < 0 or numero > 255:
            return False

    return True


# ============================================
# CLASE DISPOSITIVO
# ============================================

class Dispositivo:

    # Constructor
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip
        self.estado = "Apagado"

    # Método para encender el dispositivo
    def encender(self):
        self.estado = "Encendido"

    # Método para mostrar la información
    def mostrar_informacion(self):
        print("----- DISPOSITIVO -----")
        print("Nombre:", self.nombre)
        print("IP:", self.ip)
        print("Estado:", self.estado)


# ============================================
# PRUEBAS
# ============================================

dispositivo = Dispositivo("Router Principal", "192.168.1.1")

dispositivo.encender()

dispositivo.mostrar_informacion()

print()

print("IP válida:", validar_ip("192.168.1.1"))
print("IP inválida:", validar_ip("300.10.5.1"))