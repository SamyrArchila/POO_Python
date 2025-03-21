# Clase coordenada

class coordenada:

# Metodo constructor

 def __init__(self, x, y):  
    # Atributos privados
        self.__X = x
        self.__Y = y

# Metodo de lectura y escritura de cada atributo

def __getX(self):
    return self.__X

def getY(self):
    return self.__Y

def getx(self, x):
    self.__X = x

def gety(self, y):
    self.__y = y

# Metodo para mostrar coordenadas
    def mostrarCoordenada(self):
        print("(", self.__X, ",", self.__Y,")")

# Clase cuadrado

class cuadrado:

    # Metodo constructor
    def __init__(self,v1, v2, v3, v4):
    # Atributos privados
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # Metodos privados para mostrar los vertices

    def __mostrarCoordenadaV1(self):
        print("(", self.__V1.getX(), ",", self.__V1.getY(), ")")

    def __mostrarCoordenadaV2(self):
        print("(", self.__V2.getX(), ",", self.__V1.getY(), ")")

    def __mostrarCoordenadaV3(self):
        print("(", self.__V3.getX(), ",", self.__V1.getY(), ")")

    def __mostrarCoordenadaV4(self):
        print("(", self.__V4.getX(), ",", self.__V1.getY(), ")")

    # Metodo para mostrar los vertices

    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguentes vertices: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()

# Metodo principal del modulo

def main():
    # Input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("Digite el valor de y: "))

    # Processing
    c1 = coordenada(x1,x2)
    c1.mostrarCoordenada()

    v1 = coordenada(7,8)
    v2 = coordenada(10,8)
    v3 = coordenada(7,5)
    v4 = coordenada(10,5)

    cuadrado1 = cuadrado(v1, v2, v3 ,v4)
    cuadrado1.mostrarVertices()

    coordenada = coordenada(3,4)
    print("(", coordenada.__getX(), ",", coordenada.getY(), ")")

if __name__ == "__main__":
 main()




   






