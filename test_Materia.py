import unittest
from Profesor import Profesor
from materia import Materia, Alumno

class TestMateria(unittest.TestCase):
    def test_materia(self):
        profesor = Profesor("Alvaro Derbez", "Profesor de literatura", "53987")
        materia = Materia("Lengua y Literatura", [profesor])
        self.assertEqual(materia.obtener_profesores(), [profesor])

    def test_alumno(self):
        alumno = Alumno("Maximo Garcia ", "5643")
        self.assertEqual(alumno.obtener_nombre(), "Maximo Garcia ")
        self.assertEqual(alumno.obtener_legajo(), "5643")

    def test_materia_alumnos(self):
        materia = Materia("Estadistica", [])
        alumno1 = Alumno("Raul Boriri", "4358")
        alumno2 = Alumno("Jose Araujo", "8714")
        materia.obtener_alumnos().extend([alumno1, alumno2])
        self.assertEqual(materia.obtener_alumnos(), [alumno1, alumno2])

if __name__ == '__main__':
    unittest.main()