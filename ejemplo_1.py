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
    p2 = persona("David", "Archila", 2)
    p2.MostrarPersona()
    p1.Edad = 20
    p1.MostrarPersona()
    p1 = p2
    p1.MostrarPersona()
    p2.MostrarPersona()


if __name__ == "__main__":
    main()