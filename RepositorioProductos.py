from Producto import Producto
from RepositorioCombo import RepositorioCombo
from Combo import Combo

listProductos = []

class RepositorioProductos():

    def AgregarProducto(producto):
        
        listProductos.append(producto)

    def LongitudLista():
        return len(listProductos)
    def ObtenerProductos():
        
        for i in listProductos:

            Producto.MostrarProduc(i)
            print("\n")
            
    def ObtenerProductoEspec(codProd):
        for i in listProductos:
            if Producto.get_codProducto(i) == codProd:
                Producto.MostrarProdEspec(i)
    
    def ObtenerProdFiltro(categoria):
        if categoria == 'Combo':
                RepositorioCombo.ObtenerProdFiltro()
        elif categoria != 'Combo':    
            for i in listProductos:
                if str(Producto.get_categoria(i)) == categoria:
                    Producto.MostrarProdEspec(i)
        else:
            print("Categoria no existente.")

    def ObternerProdNom(nom):
        for i in listProductos:
            if str(Producto.get_nomProducto(i)) == nom:
                Producto.MostrarProdEspec(i)
            elif str(Producto.get_nomProducto(i)) != nom:
                RepositorioCombo.ObtenerProdNom(nom)
        else:
            print("Producto no diponible.")
            