class Voiture:
    def __init__(self, marque='Ford', couleur='rouge', pilote='personne', vitesse=0):
        self.__marque = marque
        self.__couleur = couleur
        self.__pilote = pilote
        self.__vitesse = vitesse

    def set_marque(self, marque):
        self.__marque = marque

    def set_couleur(self, couleur):
        self.__couleur = couleur

    def set_pilote(self, pilote):
        self.__pilote = pilote

    def accelerer(self, taux, duree):
        if self.__pilote != "personne":
            self.__vitesse += taux * duree
        else:
            print("Aucun pilote. La voiture ne peut pas accélérer.")

    def affiche_tout(self):
        print(f"Marque: {self.__marque}, Couleur: {self.__couleur}, Pilote: {self.__pilote}, Vitesse: {self.__vitesse} km/h")


# Programme principal
a = Voiture()

a.set_marque("BMW")
a.set_pilote("Amal")
a.set_couleur("black")
a.accelerer(2, 5)

a.affiche_tout()