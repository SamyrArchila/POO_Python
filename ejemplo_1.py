# Clase persona

class persona:
    # Metodo constructor
    def __init__(self, nombre, apellido, edad):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Edad = edad

    # Metodo para mostrar los datos de una persona

    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellidos: " + self.Apellido)
        print("Edad:" + str(self.Edad))

    # Metodo Principal
def main():
    p1 = persona("Samyr", "Archila", 15)
    p1.MostrarPersona()

if __name__ == "__main__":
    main()