from abc import ABC, abstractmethod


class Courrier(ABC):
    poids: int
    mode_expedition: str
    destination: str

    def __init__(self, poids, mode_expedition, destination):
        self.poids = poids
        self.mode_expedition = mode_expedition
        self.destination = destination

        if not (mode_expedition in ["Rapide", "Normal"]):
            raise Exception("Le mode d'expédition est Rapide ou Normal")

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def calcul_affranchissement(self):
        pass
