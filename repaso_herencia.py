class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        print("se ejecuta")

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}")


class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, carrera, year):
        super().__init__(nombre, apellido, dni)
        self.carrera = carrera
        self.year = year
        

persona = Persona("Pablo", "Sanchez", "654895622F")
persona.mostrar_datos()

estudiante = Estudiante("Juan", "Ruiz", "856249694V", "Ing. Informatica", "3")
estudiante.mostrar_datos()