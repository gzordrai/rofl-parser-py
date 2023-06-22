from enum import Enum

class Couleur(Enum):
    ROUGE: int = 1
    VERT: int = 2
    BLEU: int = 3

    def __str__(self):
        return self.name.replace("_", " ").title()

valeur = 1
couleur = Couleur(valeur)

print(couleur)  # Affiche: Couleur.ROUGE
