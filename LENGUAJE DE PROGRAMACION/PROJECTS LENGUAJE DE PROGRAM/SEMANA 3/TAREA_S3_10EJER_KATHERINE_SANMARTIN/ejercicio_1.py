# =============================================================================
# EJERCICIO 1
# Tema: Condicionales (if / elif / else)
# Salida esperada:
# protocolo = "HTTPS" -> El protocolo HTTPS es SEGURO
# protocolo = "Telnet" -> El protocolo Telnet es INSEGURO
#
# Objetivo:
# Identificar si un protocolo de red es seguro o inseguro.
#
# Aprendizaje:
# - Uso de estructuras condicionales.
# - Comparacion de cadenas de texto.
# - Uso del operador logico "or".
# - Toma de decisiones en Python.
#
# En redes es importante identificar protocolos seguros para evitar
# transmitir informacion sin cifrado.
# =============================================================================

def ejercicio_1():

    print("\n--- EJERCICIO 1: PROTOCOLO SEGURO ---")

    # Variable que almacena el protocolo a evaluar
    protocolo = "HTTPS"

    # Si el protocolo pertenece al grupo seguro
    if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP":

        print(f"El protocolo {protocolo} es SEGURO")

    # Si pertenece al grupo inseguro
    elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":

        print(f"El protocolo {protocolo} es INSEGURO")

    # Si no coincide con ninguno de los anteriores
    else:

        print("Protocolo desconocido")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a utilizar estructuras condicionales
# para evaluar diferentes casos posibles.
#
# Tambien comprendi como comparar cadenas de texto y combinar
# condiciones usando el operador logico "or".
#
# Este tipo de validaciones son utiles
# para identificar protocolos seguros e inseguros.
# =============================================================================

# Llamada de la funcion
ejercicio_1()