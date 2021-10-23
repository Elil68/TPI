import unittest
from RepositorioProductos import RepositorioProductos
from Producto import Producto

class test_1(unittest.TestCase):

    def test_guardaProductos(self):
        producto1 = Producto(123, 'nom1', 200, 'desc1', 'color1', 12, 'Yerba')
        RepositorioProductos.AgregarProducto(producto1)
        producto2 = Producto(345, 'nom2', 900, 'desc2', 'color2', 30, 'Mate')
        RepositorioProductos.AgregarProducto(producto2)
        producto3 = Producto(567, 'nom3', 600, 'desc3', 'color3', 40, 'Termo')
        RepositorioProductos.AgregarProducto(producto3)
        
        self.assertEqual(3, RepositorioProductos.LongitudLista())

    
if __name__ == "__main__":
    unittest.main()
