from Combo import Combo

listCombo = []

class RepositorioCombo():

    def AgregarCombo(combo):
        listCombo.append(combo)

    def ObtenerCombo():
        
        for i in listCombo:
            Combo.MostrarCombo(i)
            print("\n")

    def ObtenerComboEspec(codCombo):
        for i in listCombo:
            if Combo.get_codCombo(i) == codCombo:
                Combo.MostrarComboEspec(i)

    def ObtenerProdFiltro():
        for i in listCombo: 
            Combo.MostrarComboEspec(i)

    def ObtenerProdNom(nom):
        for i in listCombo:
            if str(Combo.get_nomCombo(i)) == nom:
                Combo.MostrarComboEspec(i)

    def LongitudLista():
        return len(listCombo)
        