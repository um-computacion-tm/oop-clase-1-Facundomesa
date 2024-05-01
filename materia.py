class Alumno:
    def __init__(self, nombre, legajo):
        self.__nombre__ = nombre
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_legajo(self):
        return self.__legajo__

class Materia:
    def __init__(self, nombre, profesores):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = []

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__