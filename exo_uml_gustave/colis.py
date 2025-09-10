from courrier import Courrier


class Colis(Courrier):
    volume: float

    def __init__(self, poids, mode_expedition, destination, volume):
        self.volume = volume
        super().__init__(poids, mode_expedition, destination)

    def __str__(self):
        return (
            "colis de "
            + str(self.poids)
            + " grammes, mode d'expédition "
            + self.mode_expedition
            + ", à destination de " + self.destination
            + ", de volume "
            + str(self.volume)
        )

    def calcul_affranchissement(self):
        tarif = self.volume / 4 + self.poids * 0.001
        if self.mode_expedition == "Rapide":
            tarif = 2 * tarif
        return tarif


if __name__ == "__main__":
    poids = 40
    mode_expedition = "Rapide"
    destination = "3 rue des Lilas"
    volume = 5

    colis = Colis(poids, mode_expedition, destination, volume)

    print(colis)

    prix = colis.calcul_affranchissement()
    print(prix)
