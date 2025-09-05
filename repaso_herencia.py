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

    def mostrar_datos4(self):
        #super().mostrar_datos()
        print(f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Carrera: {self.carrera}, Año: {self.year}")

class Empleado(Estudiante):
    def __init__(self, nombre, apellido, dni, carrera, year, area, sueldo):
        super().__init__(nombre, apellido, dni, carrera, year)
        self.area = area
        self.sueldo = sueldo

    def mostrar_datos5(self):
        super().mostrar_datos4()
        print(f"Area: {self.area}, Sueldo: {self.sueldo}")

persona = Persona("Pablo", "Sanchez", "654895622F")
persona.mostrar_datos()

estudiante = Estudiante("Juan", "Ruiz", "856249694V", "Ing. Informatica", "3")
estudiante.mostrar_datos4()

empleado = Empleado("Maria", "Perez", "52536895X", "Ing. Comercial", "2", "Informatica", "3000")
empleado.mostrar_datos5()