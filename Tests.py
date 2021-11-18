import unittest
import json
from RepositorioProductos import RepositorioProductos
from Producto import Producto
from datetime import datetime
from RepositorioCombo import RepositorioCombo
from Combo import Combo
from datetime import datetime

class test_1(unittest.TestCase):

    def test_guardaProductos(self):
        with open('Productos.json') as file:
            productos = json.load(file)
            
            for i in productos['productos']:
                cP = i['codProducto']
                nP = i['nomProducto']
                pre = i['precio']
                des = i['desc']
                co = i['color']
                st = i['stockProducto']
                cat = i['categoria']
                preDC = i['precioDosCinco']
                preSD = i['precioSeisDiez']
                preDM = i['precioDiezMas']
                estado = i['estaOferta']
                desO = i['desOferta']
                preO = i['precioOferta']
                feI = i['fechaInOferta']
                fechaI = datetime.strptime(feI, '%Y-%m-%dT%H:%M:%S')
                feF = i['fechaFinOferta']
                fechaFin = datetime.strptime(feF, '%Y-%m-%dT%H:%M:%S')
            
                produc = Producto(cP, nP, pre, des, co, st, cat, preDC, preSD, preDM, estado, desO, preO, fechaI, fechaFin)
                RepositorioProductos.AgregarProducto(produc)
        
        self.assertEqual(3, RepositorioProductos.LongitudLista())
    
    def test_guardaCombos(self):
        with open('Combos.json') as file:
            combos = json.load(file)
            
            for i in combos['combos']:
                cC = i['CodigoCombo']
                nC = i['NombreCombo']
                pre = i['Precio']
                des = i['Descripcion']
                st = i['Stock']
            
                comb = Combo(cC, nC, pre, des, st, 'Combo')
                RepositorioCombo.AgregarCombo(comb)
        
        self.assertEqual(3, RepositorioCombo.LongitudLista())
    
    def test_ofertasDentroRangoFecha(self):

        producto = Producto(1, 'nom', 123, 'desc', 'color', 213, 'cate', 123, 123, 123, True, 'desOferta', 123, datetime(2021, 11, 16), datetime(2021, 11, 30))
        RepositorioProductos.AgregarProducto(producto)

        self.assertTrue(RepositorioProductos.ObtenerOferta(datetime(2021, 11, 14)))
    
    def test_ofertasFueraRangoFecha(self):
        
        producto = Producto(1, 'nom', 123, 'desc', 'color', 213, 'cate', 123, 123, 123, True, 'desOferta', 123, datetime(2021, 11, 16), datetime(2021, 11, 30))
        RepositorioProductos.AgregarProducto(producto)
        
        self.assertFalse(RepositorioProductos.ObtenerOferta(datetime(2021, 12, 20)))

    def test_mostrarProductosFiltradosPorCategoria(self):
        producto1 = Producto(1, 'nom1', 123, 'desc', 'color', 213, 'Mate', 123, 123, 123, True, 'desOferta', 123, datetime(2021, 11, 16), datetime(2021, 11, 30))
        RepositorioProductos.AgregarProducto(producto1)
        producto2 = Producto(2, 'nom2', 123, 'desc', 'color', 213, 'Termo', 123, 123, 123, True, 'desOferta', 123, datetime(2021, 11, 16), datetime(2021, 11, 30))
        RepositorioProductos.AgregarProducto(producto2)
        producto3 = Producto(3, 'nom3', 123, 'desc', 'color', 213, 'Mate', 123, 123, 123, True, 'desOferta', 123, datetime(2021, 11, 16), datetime(2021, 11, 30))
        RepositorioProductos.AgregarProducto(producto3)

        self.assertEqual(2, RepositorioProductos.ObtenerProdFiltro('Mate'))
if __name__ == "__main__":
    unittest.main()
