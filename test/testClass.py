class Demo:
    def __init__(self, valeur):
        self.val_1 = valeur.valeur_1
        self.val_2 = valeur.valeur_2
        self.val_3 = valeur.valeur_3

        print(self.val_1, self.val_2, self.val_3)


class Test:
    valeur_1 = "texte_valeur_1"
    valeur_2 = "texte_valeur_2"
    valeur_3 = "texte_valeur_3"


arguments = Test()
d = Demo(valeur=arguments)
