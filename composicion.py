# Composicion

"""- Una coordenada en dos dimensiones esta compuesta por dos valores el valor en el eje de las X y el valor del eje Y, esto podria ser una clase. 
Un cuadrado esta compuesto por cuatro coordenadas que son los 4 vertices, 
esto podria ser una clase que esta compuesta por cuatro clases del objeto 
coordenada"""

# Clase coordenada

class Coordenada:
    # Metodo constructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # Metodo para mostrar coordenadas
    def mostrarCoordenada(self):
        print("(", self.X, ",", self.Y,")")

# Clase cuadrado

class cuadrado:

    # Metodo constructor
    def __init__(self,v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    # Metodo para mostrar los vertices
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguentes vertices: ")
        self.V1.mostrarCoordenada()
        self.V2.mostrarCoordenada()
        self.V3.mostrarCoordenada()
        self.V4.mostrarCoordenada()

# Metodo principal
def main():
    # Input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("Digite el valor de y: "))

    # Processing
    c1 = Coordenada(x1,x2)
    c1.mostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = cuadrado(v1, v2, v3 ,v4)
    cuadrado1.mostrarVertices()

if __name__ == "__main__":
    main()


        
