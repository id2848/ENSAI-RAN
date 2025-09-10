from courrier import Courrier


class Lettre(Courrier):
    format: str

    def __init__(self, poids, mode_expedition, destination, format):
        if not (format in ["A3", "A4"]):
            raise Exception("Le format doit être A3 ou A4")
        self.format = format
        super().__init__(poids, mode_expedition, destination)

    def __str__(self):
        return (
            "lettre de "
            + str(self.poids)
            + " grammes, mode d'expédition "
            + self.mode_expedition
            + ", à destination de " + self.destination
            + ", de format "
            + self.format

        )
        
    def calcul_affranchissement(self):
        if self.format == "A4":
            tarif_base = 2.5
        else:
            tarif_base = 3.5
        tarif = tarif_base + self.poids * 0.001
        if self.mode_expedition == "Rapide":
            tarif = 2 * tarif
        return tarif


if __name__ == "__main__":
    poids = 40
    mode_expedition = "Rapide"
    destination = "3 rue des Lilas"
    format = "A3"

    lettre = Lettre(poids, mode_expedition, destination, format)

    print(lettre)

    prix = lettre.calcul_affranchissement()
    print(prix)
