import json
from datetime import datetime
from Producto import Producto
from Combo import Combo
from RepositorioCombo import RepositorioCombo
from RepositorioProductos import RepositorioProductos


class DTO():
    def CrearObjetos():
        
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