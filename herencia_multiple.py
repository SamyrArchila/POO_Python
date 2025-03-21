class DispositivoElectronico:

    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print(f"El dispositivo {self.marca} está encendido.")

class Comunicacion:

    def hacer_llamada(self, numero):
        print(f"Llamando al número {numero}...")

class TelefonoMovil(DispositivoElectronico, Comunicacion):
    
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    def mostrar_modelo(self):
        print(f"El modelo de este teléfono es {self.modelo}.")

mi_telefono = TelefonoMovil("Samsung", "Galaxy S23")
mi_telefono.encender()        
mi_telefono.hacer_llamada("3214567890")  
mi_telefono.mostrar_modelo()  