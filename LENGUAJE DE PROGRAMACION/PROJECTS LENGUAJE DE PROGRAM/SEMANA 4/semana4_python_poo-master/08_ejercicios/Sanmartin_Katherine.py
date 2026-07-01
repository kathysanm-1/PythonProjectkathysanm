class Dispositivo:
    def __init__(self, ip,mac):
        self.ip = ip
        self.mac = mac

    def reportar (self):
        print(f"IP: {self.ip}, MAC: {self.mac}")


    def validar(self):
        if "abcdefghijklmnop"in self.ip:
            return False
        else:
            return True


llamada_dispositivo = Dispositivo("localhost",9999)
es_valida_ = llamada_dispositivo.es_valida  ()
print(es_valida_)

