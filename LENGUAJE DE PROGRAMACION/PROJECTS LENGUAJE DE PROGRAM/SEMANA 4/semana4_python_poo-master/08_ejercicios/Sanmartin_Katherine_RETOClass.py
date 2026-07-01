class ImpresoraRed:
    def __init__(self, ip, modelo):
        # Guardamos la IP de la impresora
        self.ip = ip
        # Guardamos el modelo
        self.modelo = modelo
        # La impresora inicia con 0 páginas impresas
        self.paginas_impresoras = 0

    # Metodo para imprimir páginas
    def imprimir(self, cantidad):

        # Validamos que la cantidad sea positiva
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero")
            return
        # Sumamos las páginas impresas
        self.paginas_impresoras += cantidad

    # Metodo para mostrar información
    def reportar(self):
        print(f"IP: {self.ip}")
        print(f"Modelo: {self.modelo}")
        print(f"Paginas impresoras: {self.paginas_impresoras}")

# ----------------------------------
# PRUEBAS DEL EJERCICIO
# ----------------------------------
    #Crear objeto (fuera de la clase)

imp = ImpresoraRed("10.0.0.50", "HP-LaserJet")

imp.imprimir(-3)
imp.imprimir(3)
imp.imprimir(5)

imp.reportar()