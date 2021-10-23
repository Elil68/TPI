

class Producto():
    def __init__(self, codProducto, nomProducto, precio, desc, color, stockProducto, categoria):

        self.__codProducto = codProducto
        self.__nomProducto = nomProducto
        self.__precio = precio
        self.__desc = desc
        self.__color = color
        self.__stockProducto = stockProducto
        self.__categoria = categoria 

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
            print(self.__nomProducto, self.__precio, self.__desc, self.__color, self.__categoria, self.__stockProducto)
        else:
            print("Producto sin stock.")

    def __str__(self):
        return f"{self.__nomProducto}, {self.__precio}, {self.__desc}, {self.__color}, {self.__categoria}, {self.__stockProducto}"
        