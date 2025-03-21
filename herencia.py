# Clase Persona

class Persona:
    
    # método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))

class Alumno(Persona):
    def __init__(self):
        self.__Curso = ""
        self.__Asignaturas = ""
    
    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def mostrarAlumno(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", self.__Asignaturas)

class Profesor(Persona):
    def __init__(self):
        self.__antiguedad = 0
        self.__tutorias = 0
        self.__telefono = 0

    def getAntiguedad(self):
        return self.__antiguedad
    
    def setAntiguedad(self, antiguedad):
        self.__antiguedad = antiguedad

    def getTutorias(self):
        return self.__tutorias
    
    def setTutorias(self, tutorias):
        self.__Tutorias = tutorias

    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, telefono):
        self.__Telefono = telefono

    def mostrarProfesor(self):
        print("Alumno")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tAntiguedad: ", self.__antiguedad)
        print("\tTutorias: ", self.__Tutorias) 
        print("\tTelefono: ", self.__Telefono)


# metodo principal
def main():
    alumno = Alumno()
    alumno.setNombre("Samyr Alejandro")
    alumno.setApellidos("Archila Guiza")
    alumno.setEdad(15)
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés", "Español", "Sistemas"])
    alumno.mostrarAlumno()

# Profesor

    profesor = Profesor ()
    profesor.setNombre("Néstor")
    profesor.setApellidos("Páez Sarmiento")
    profesor.setEdad(30)
    profesor.setAntiguedad(12)
    profesor.setTutorias(["Lunes de 7 am a 1 pm", "Miercoles de 8 am a 2 pm", "Viernes de 7:30 am a 1:30 pm"])
    profesor.setTelefono("32223315223")
    profesor.mostrarProfesor()


if __name__ == "__main__":
    main()