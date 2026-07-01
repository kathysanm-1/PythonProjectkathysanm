#---------------------------
#CLASE ROUTER
#---------------------------

class Router:
    # Constructor: se ejecuta cuando creamos un objeto Router
    def __init__(self, ip, modelo):
    # Guardamos la IP recibida
        self.ip = ip

    #Guardamos el modelo recibido
        self.modelo = modelo

    #El router empieza con 0 rutas configuradas
        self.rutas_configuradas = 0

# Metodo para agregar rutas
    def agregar_ruta(self, cantidad):

    #Validamoss que la cantidad se mayor a 0
        if cantidad <= 0:
            print("Error: la cantidad de rutas debe ser mayor que cero")
            return
    #Sumamos la cantidad al total de rutas configuradas
        self.rutas_configuradas += cantidad

#Metodo para mostrar la información del router
    def reportar(self) :

        print(
        f"IP: {self.ip}, "
        f"Modelo: {self.modelo}, "
        f"Rutas: {self.rutas_configuradas}"
        )

# ------------------------------------
# PRUEBAS DEL EJERCICIO
# ------------------------------------

# Crear un router

router1 = Router(
    "192.168.1.1",
    "Cisco-2960"
)

# Agregar 2 rutas
router1.agregar_ruta(2)

# Agregar 4 rutas
router1.agregar_ruta(4)

# Agregar 1 ruta
router1.agregar_ruta(1)

# Mostrar información final
router1.reportar()
