from RepositorioCombo import RepositorioCombo
from RepositorioProductos import RepositorioProductos
from datetime import datetime



class Facade():
    
    def MostrarOfertasHoy(): #funcion de funcionamiento real, la funcionalidad real seria mostrar cuando coincide el dia actual con alguno de los productos almacenados con fecha de oferta de ese dia.
        fecha = datetime.today()
        RepositorioProductos.ComprobarProducOferta(fecha)
        

    def MostrarOfertas(): #funcion para probar Mostrar ofertas
        print("Ingresar fecha: ")
        dia = int(input("Dia: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))

        fecha = datetime(anio, mes, dia)
        RepositorioProductos.ComprobarProducOferta(fecha)
        
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
        

