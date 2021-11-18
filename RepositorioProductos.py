from Producto import Producto
from RepositorioCombo import RepositorioCombo


listProductos = []

class RepositorioProductos():

    def AgregarProducto(producto):
        
        listProductos.append(producto)

    def LongitudLista():
        return len(listProductos)

    def BuscarProducto(produc):
        for i in listProductos:
            return i 

    def ObtenerProductos():
        
        for i in listProductos:

            Producto.MostrarProduc(i)
            print("\n")
            
    def ObtenerProductoEspec(codProd):
        for i in listProductos:
            if Producto.get_codProducto(i) == codProd:
                Producto.MostrarProdEspec(i)
    
    def ObtenerProdFiltro(categoria):
        j = 0
        if categoria == 'Combo':
                RepositorioCombo.ObtenerProdFiltro()
                j = j + 1
        elif categoria != 'Combo':    
            for i in listProductos:
                if str(Producto.get_categoria(i)) == categoria:
                    j = j+ 1
                    Producto.MostrarProdEspec(i)
        else:
            print("Categoria no existente.")
        return j

    def ObternerProdNom(nom):
        for i in listProductos:
            if str(Producto.get_nomProducto(i)) == nom:
                Producto.MostrarProdEspec(i)
            elif str(Producto.get_nomProducto(i)) != nom:
                RepositorioCombo.ObtenerProdNom(nom)
        else:
            print("Producto no diponible.")
            
    def ComprobarProducOferta(fecha):
        for i in listProductos:
            if fecha >= Producto.get_fechaInOferta(i) and fecha <= Producto.get_fechaFinOferta(i):
                print(Producto.MostrarOfertas(i))
            else:
                return print('No hay ofertas este dia.')
                
    def ObtenerOferta(fecha):
        for i in listProductos:
            if fecha >= Producto.get_fechaInOferta(i) and fecha < Producto.get_fechaFinOferta(i):
                return True
            else:
                return False
        