from Facade import Facade
from DTO import DTO


DTO.CrearObjetos()
print("-------------------Ofertas de hoy-------------------")
Facade.MostrarOfertasHoy()
print("-------------------Productos-------------------")
Facade.MostrarProductos()
print("--------------------Combos--------------------")
Facade.MostrarCombos()



menu = input("1. Mostrar un producto en especifico. \n2. Mostrar un combo en especifico. \n3. Mostrar productos por categoria. \n4. Mostrar productos por nombre. \n5. Mostrar Ofertas.(para probar mostrar ofertas)\n0. Salir")
while menu != '0':
    if menu == '1':
        Facade.MostrarProductoEspec()
    elif menu == '2':
        Facade.MostrarComboEspec()
    elif menu == '3':
        Facade.MostrarProdFiltro()
    elif menu == '4':
        Facade.MostrarProdNom()
    elif menu == '5':
        Facade.MostrarOfertas()
    else:
        print("Opcion no valida.")
    print("\n")
    menu = input("1. Mostrar un producto en especifico. \n2. Mostrar un combo en especifico. \n3. Mostrar productos por categoria. \n4. Mostrar productos por nombre. \n5. Mostrar Ofertas.(para probar mostrar ofertas)\n0. Salir")

    