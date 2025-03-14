# POO en Python
Introduccion a la POO en Python

- El paradigma POO esta basado en una abstracion del mundo real que nos va a permitir desarrollar programas de formas mas cercanas de como conocemos el mundo pensando en objetos que tenemos delante y en       acciones que podamos hacer con ellos

## Clase

- Una clase es un tipo de dato cuyas variables se llaman objetos o instancias 

- la clase es la definicion del concepto del mundo real y los objetos o instancias son el propio objeto del mundo real

- Las clases estan compuestas por dos elementos:
Atributos
metodos

### Atributos

- informacion que almacena la clase 

### Metodos

- Operaciones que puede realizar las clases

##  Definicion de una clase en Python
```Python
class NombreClase:
    def __init__(self, variable1, variable2):
    self.Atributo1 = valor1
    self.Atributo2 = valor2

    def NombreMetodo(self):
   BloqueCodigo
```

### Componentes

```class```: Palabra reservada en Python para reprimir una clase

```NombreClase```: Nombre de clase que quieres crear

```def```: Palabra reservada en Python que se utiliza para definir un contructor de la clase (Metodo que se ejecuta la primera vez que  usas en una clase) como los diferentes metodos que tiene.

```__init__```: Palabra reservada en python para definir el metodo contructor de la clase. Es el metodo que es lo primero que se ejecuta cuando creas un objeto de una clase.

```(self, variableX)```: Parametro del contructor de la clase. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones

```self.AtributoX```: Forma de ultilizacion y acceso a los atributos de la clase

```NombreMetodo```: Nombre del metodo de la clase

```(self)```: Parametros del metodo. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones

```BloqueCodigo```: Instrucciones que ejecutara el metodo.

- Cuando defines una clase debes tener en cuenta los siguentes puntos:

    - Puedes definir tantos atributos como necesites
    - Puedes definir tantos metodos como necesites
    - Puedes definir tantos parametros en el contructor y en los metodos que necesites

## Composicion

- Consiste en la creacion de nuevas clases a partir de otras clases ya existentes que actuan como elemento de compositores de la nueva

- Las clases existentes seran atributos de la nueva clase

- En POO la composicion significa que en las dos clases existe una relacion de tipo "Tiene 1".

- Ejemplo:
    - Una coordenada en dos dimensiones esta compuesta por dos valores el valor en el eje de las X y el valor del eje Y, esto podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que son los 4 vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada






