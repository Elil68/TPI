class Categoria():
    def __init__(self, nomCategoria):
        
        self.__nomCategoria = nomCategoria
        

    def get_nomCategoria(self):
        return self.__nomCategoria
    def set_nomCategoria(self, nomCategoria):
        self.__nomCategoria = nomCategoria

    def __str__(self):
        return f"{self.__nomCategoria}"
        