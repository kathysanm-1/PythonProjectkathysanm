"""
Estudiante: Valeria SanMartín
Fecha: 30/06/2026
Asignatura: Lenguaje de Programación Python

Propósito:
Sistema de inventario de dispositivos de red.

Uso de IA:
Se utilizó ChatGPT como apoyo para comprender la implementación
de funciones, métodos y pilares de la Programación Orientada a Objetos.
Todo el codigo fue revisado y comprendido antes de su entrega.
"""

# ==========================================
# TIPO 1: FUNCIÓN SUELTA
# ==========================================

def imprimir_banner():
    print("=" * 60)
    print("           SISTEMA DE INVENTARIO DE DISPOSITIVOS ")
    print("=" * 60)
#imprimir_banner()

# ==========================================
# CLASE DISPOSITIVO
# ==========================================

class Dispositivo:

    # Constructor
    def __init__(self, ip, modelo, ubicacion):

        # Estos atributos pertenecen al objeto
        self.modelo = modelo
        self.ubicacion = ubicacion

        # La IP se asigna mediante el setter
        self.ip = ip


# ==========================================
# TIPO 3: @property
# ==========================================

    @property
    def ip(self):
        # Devuelve la IP almacenada
        return self._ip


    @ip.setter
    def ip(self, valor):

        # Separamos la IP por los puntos
        partes = valor.split(".")

        # Debe tener exactamente 4 partes
        if len(partes) != 4:
            raise ValueError("IP inválida: " + valor)

        # Revisamos cada parte
        for parte in partes:

            # Debe ser un número
            if not parte.isdigit():
                raise ValueError("IP inválida: " + valor)

            numero = int(parte)

            # Debe estar entre 0 y 255
            if numero < 0 or numero > 255:
                raise ValueError("IP inválida: " + valor)

        # Si todo esta correcto, guardamos la IP
        self._ip = valor

# ==========================================
# TIPO 2: METODO NORMAL
# ==========================================

    def reportar(self):

        print("\nInformación del dispositivo")
        print("----------------------------")
        print("IP:", self.ip)
        print("Modelo:", self.modelo)
        print("Ubicación:", self.ubicacion)

    # ==========================================
    # TIPO 4: @staticmethod
    # ==========================================

    @staticmethod
    def es_ip_privada(ip):

        # Si empieza con 10., es privada
        if ip.startswith("10."):
            return True

        # Si empieza con 192.168., es privada
        if ip.startswith("192.168."):
            return True

        # Revisamos el rango 172.16.x.x hasta 172.31.x.x
        partes = ip.split(".")

        if len(partes) == 4:

            if partes[0] == "172":

                segundo_octeto = int(partes[1])

                if 16 <= segundo_octeto <= 31:
                    return True

        # Si no cumple ningún caso
        return False

# ==========================================
    # TIPO 5: @classmethod
    # ==========================================

    @classmethod
    def desde_csv(cls, linea):

        # Dividimos la línea del archivo CSV
        ip, modelo, ubicacion = linea.split(",")

        # Eliminamos espacios innecesarios
        ip = ip.strip()
        modelo = modelo.strip()
        ubicacion = ubicacion.strip()

        # Creamos y devolvemos un nuevo objeto
        return cls(ip, modelo, ubicacion)

# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

if __name__ == "__main__":

    # Mostrar el banner
    imprimir_banner()

    print()

    # Crear un dispositivo manualmente
    dispositivo1 = Dispositivo(
        "10.0.0.1",
        "Cisco-2960",
        "DC-A"
    )

    # Crear un dispositivo desde una línea CSV
    dispositivo2 = Dispositivo.desde_csv(
        "192.168.1.1, MikroTik, Oficina"
    )

    # Mostrar la información de ambos dispositivos
    dispositivo1.reportar()

    print()

    dispositivo2.reportar()

    print()

    # Probar si las IP son privadas
    print("10.0.0.5 es privada?:",
          Dispositivo.es_ip_privada("10.0.0.5"))

    print("8.8.8.8 es privada?:",
          Dispositivo.es_ip_privada("8.8.8.8"))

    print()

    # Probar una IP inválida
    try:

        dispositivo3 = Dispositivo(
            "999.0.0.1",
            "Cisco",
            "Laboratorio"
        )

    except ValueError as e:

        print("Error capturado:", e)