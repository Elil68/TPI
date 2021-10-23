from RepositorioCombo import RepositorioCombo
from Combo import Combo
from RepositorioProductos import RepositorioProductos
from Categoria import Categoria
from Producto import Producto
class Facade():


    def MostrarProductos():
        RepositorioProductos.ObtenerProductos()
    
    def MostrarCombos():
        RepositorioCombo.ObtenerCombo()

    def MostrarProductoEspec():
        codProd = int(input("Codigo producto: "))
        RepositorioProductos.ObtenerProductoEspec(codProd)
    
    def MostrarComboEspec():
        codCombo = int(input("Codigo combo: "))
        RepositorioCombo.ObtenerComboEspec(codCombo)

    def MostrarProdFiltro():
        categoria = input("Categoria: ")
        RepositorioProductos.ObtenerProdFiltro(categoria)

    def MostrarProdNom():
        nom = input("Buscar Producto por nombre: ")
        RepositorioProductos.ObternerProdNom(nom)
        
    def CrearObjetos():
        categoria1 = Categoria('Yerba')
        categoria2 = Categoria('Mate')
        categoria3 = Categoria('Termo')
        categoria4 = Categoria('Bombilla')
        categoriaCombo = Categoria('Combo')

        producto1 = Producto(123, 'Nom1', 200, 'desc1', 'color1', 12, categoria1)
        RepositorioProductos.AgregarProducto(producto1)
        producto2 = Producto(345, 'Nom2', 900, 'desc2', 'color2', 30, categoria2)
        RepositorioProductos.AgregarProducto(producto2)
        producto3 = Producto(567, 'Nom3', 600, 'desc3', 'color3', 40, categoria3)
        RepositorioProductos.AgregarProducto(producto3)
        producto4 = Producto(904, 'Nom4', 100, 'desc4', 'color4', 10, categoria1)
        RepositorioProductos.AgregarProducto(producto4)
        producto5 = Producto(674, 'Nom5', 1500, 'desc5', 'color1', 5, categoria3)
        RepositorioProductos.AgregarProducto(producto5)
        producto6 = Producto(195, 'Nom6', 2000, 'desc6', 'color2', 0, categoria4)
        RepositorioProductos.AgregarProducto(producto6)
        producto7 = Producto(819, 'Nom7', 300, 'desc7', 'color3', 100, categoria2)
        RepositorioProductos.AgregarProducto(producto7)

        combo1 = Combo(321, 'Combo1', 300, 'desc1', 3, categoriaCombo)
        RepositorioCombo.AgregarCombo(combo1)
        combo2 = Combo(894, 'Combo2', 1000, 'desc2', 100, categoriaCombo)
        RepositorioCombo.AgregarCombo(combo2)
        combo3 = Combo(143, 'Combo3', 2500, 'desc3', 200, categoriaCombo)
        RepositorioCombo.AgregarCombo(combo3)
        combo4 = Combo(937, 'Combo4', 200, 'desc4', 0, categoriaCombo)
        RepositorioCombo.AgregarCombo(combo4)
        combo5 = Combo(381, 'Combo5', 800, 'desc5', 50, categoriaCombo)
        RepositorioCombo.AgregarCombo(combo5)
     
        

