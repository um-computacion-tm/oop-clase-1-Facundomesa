import unittest
from Profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_profesor(self):
        
        profesor = Profesor("Luis Silva", "Profesor de Biologia", "5021")
        self.assertEqual(profesor.obtener_nombre(), "Luis Silva") 
        self.assertEqual(profesor.obtener_cargo(), "Profesor de Biologia")
        self.assertEqual(profesor.obtener_legajo(), "5021")

if __name__ == '__main__':
    unittest.main()