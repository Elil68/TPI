
class Producto():
    def __init__(self, codProducto, nomProducto, precio, desc, color, stockProducto, categoria, precioDosCinco, precioSeisDiez, precioDiezMas, estaOferta, desOferta, precioOferta, fechaInOferta, fechaFinOferta):

        self.__codProducto = codProducto
        self.__nomProducto = nomProducto
        self.__precio = precio
        self.__desc = desc
        self.__color = color
        self.__stockProducto = stockProducto
        self.__categoria = categoria
        self.__precioDosCinco = precioDosCinco
        self.__precioSeisDiez = precioSeisDiez
        self.__precioDiezMas = precioDiezMas
        self.__estaOferta = estaOferta
        self.__desOferta = desOferta
        self.__precioOferta = precioOferta
        self.__fechaInOferta = fechaInOferta
        self.__fechaFinOferta = fechaFinOferta

    def get_precioDosCinco(self):
        return self.__precioDosCinco
    def set_precioDosCinco(self, precioDosCinco):
        self.__precioDosCinco = precioDosCinco

    def get_precioSeisDiez(self):
        return self.__precioSeisDiez
    def set_precioSeisDiez(self, precioSeisDiez):
        self.__precioSeisDiez = precioSeisDiez
    
    def get_precioDiezMas(self):
        return self.__precioDiezMas
    def set_precioDiezMas(self, precioDiezMas):
        self.__precioDiezMas = precioDiezMas
    
    def get_estaOferta(self):
        return self.__estaOferta
    def set_estaOferta(self, estaOFerta):
        self.__estaOferta = estaOFerta

    def get_desOferta(self):
        return self.__desOferta
    def set_desOferta(self, desOferta):
        self.__desOferta = desOferta
    
    def get_precioOferta(self):
        return self.__precioOferta
    def set_precioOferta(self, precioOferta):
        self.__precioOferta = precioOferta

    def get_fechaInOferta(self):
        return self.__fechaInOferta
    def set_fechaInOferta(self, fechaInOferta):
        self.__fechaInOferta = fechaInOferta
    
    def get_fechaFinOferta(self):
        return self.__fechaFinOferta
    def set_fechaFinOferta(self, fechaFinOferta):
        self.__fechaFinOferta = fechaFinOferta

    def get_codProducto(self):
        return self.__codProducto
    def set_codProducto(self, codProducto):
        self.__codProducto = codProducto

    def get_nomProducto(self):
        return self.__nomProducto
    def set_nomProducto(self, nomProducto):
        self.__nomProducto = nomProducto

    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio

    def get_desc(self):
        return self.__desc
    def set_desc(self, desc):
        self.__desc = desc

    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_stockProducto(self):
        return self.__stockProducto
    def set_stockProducto(self, stockProducto):
        self.__stockProducto = stockProducto

    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, categoria):
        self.__categoria = categoria
    
    def MostrarProduc(self):
        if self.__stockProducto > 0:
            
            print(self.__nomProducto, self.__precio)

    def MostrarProdEspec(self):
        if self.__stockProducto > 0:
            print('\n')
            print(self.__nomProducto, self.__precio, self.__desc, self.__color, self.__categoria, self.__stockProducto)
        else:
            print("Producto sin stock.")

    def MostrarOfertas(self):
        print('\n')
        return f"{self.__nomProducto} \nPrecio de Oferta: {self.__precioOferta} \nPrecio de compras entre Dos y Cinco unidades: {self.__precioDosCinco} \nPrecio de compras entre Seis y Diez unidades: {self.__precioSeisDiez} \nPrecio de compras entre Diez o MAS unidades: {self.__precioDiezMas} \nOferta validad hasta: {self.__fechaFinOferta} \nCantidad disponible: {self.__stockProducto}"

    def __str__(self):
        return f"{self.__nomProducto}, {self.__precio}, {self.__desc}, {self.__color}, {self.__categoria}, {self.__stockProducto}"
        