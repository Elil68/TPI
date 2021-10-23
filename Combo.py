from Categoria import Categoria


class Combo():
    def __init__(self, codCombo, nomCombo, precioCombo, desc, stockCombo, categoria):
        
        self.__codCombo = codCombo
        self.__nomCombo = nomCombo
        self.__precioCombo = precioCombo
        self.__desc = desc
        self.__stockCombo = stockCombo
        self.__categoria = categoria
        
    def get_codCombo(self):
        return self.__codCombo
    def set_codCombo(self, codCombo):
        self.__codCombo = codCombo

    def get_nomCombo(self):
        return self.__nomCombo
    def set_nomCombo(slef, nomCombo):
        slef.__nomCombo = nomCombo
    
    def get_precioCombo(self):
        return self.__precioCombo
    def set_precioComob(self, precioCombo):
        self.__precioCombo = precioCombo

    def get_desc(self):
        return self.__desc
    def set_desc(self, desc):
        self.__desc = desc
    
    def get_stockCombo(self):
        return self.__stockCombo
    def set_stockCombo(self, stockCombo):
        self.__stockCombo = stockCombo
    
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self, categoria):
        self.__categoria = categoria
        
    def MostrarCombo(self):
        if self.__stockCombo > 0:
            print(self.__nomCombo, self.__precioCombo)
    
    def MostrarComboEspec(self):
        if self.__stockCombo > 0:
            print(self.__nomCombo, self.__precioCombo, self.__desc, self.__stockCombo)
        else: 
            print("Combo sin stock.")
