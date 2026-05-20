# =============================================================================
# EJERCICIO 10
# Tema: Integrador (if + for + cadenas + validaciones)
# Salida esperada:
# 192.168.1.1 -> Valida
# 10.0.0.255 -> Valida
# 256.1.1.1 -> Invalida (octeto fuera de rango)
# 192.168.1 -> Invalida (faltan octetos)
# 192.168.a.1 -> Invalida (no numerico)
#
# Objetivo:
# Validar si una direccion IPv4 es correcta.
#
# Aprendizaje:
# - Uso de if y for combinados.
# - Manipulacion de cadenas.
# - Uso de split().
# - Uso de isdigit().
# - Validacion de rangos numericos.
#
# Las direcciones IP son fundamentales.
# Validarlas correctamente es importante para evitar
# errores de configuracion y problemas de conectividad.
# =============================================================================

def ejercicio_10():

    print("\n--- EJERCICIO 10: VALIDAR IPv4 ---")

    # Lista de IPs para probar
    ips = [
        "192.168.1.1",
        "10.0.0.255",
        "256.1.1.1",
        "192.168.1",
        "192.168.a.1"
    ]

    # Recorrer todas las IPs
    for ip in ips:

        # split(".") divide la IP usando el punto
        partes = ip.split(".")

        # Variable que indica si la IP es valida
        valida = True

        # Verificar que existan exactamente 4 octetos
        if len(partes) != 4:

            valida = False

        else:

            # Revisar cada octeto
            for octeto in partes:

                # Verificar que sea numerico
                if not octeto.isdigit():

                    valida = False
                    break

                # Convertir texto a numero
                valor = int(octeto)

                # Validar rango permitido
                if valor < 0 or valor > 255:

                    valida = False
                    break

        # Resultado final
        if valida:

            print(f"{ip} -> Valida")

        else:

            print(f"{ip} -> Invalida")


# =============================================================================
# CONCLUSION DEL EJERCICIO
# =============================================================================
# En este ejercicio aprendi a combinar estructuras
# condicionales, bucles y validaciones en un solo programa.
#
# Tambien comprendi como manipular cadenas utilizando split()
# y validar datos numericos mediante isdigit().
#
# Este tipo de validaciones son fundamentales
# para verificar direcciones IP correctas.
# =============================================================================


# Llamada de la funcion
ejercicio_10()