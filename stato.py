from enum import Enum

class TipoStato(Enum):
    Iniziale = 1
    Finale = 2
    Nullo = 3


class Stato:
    def __init__(self, id, tipo_stato):
        self.id = id
        self.tipo = tipo_stato

    # Per stampare le clssi per debuggare/capire
    # def __str__(self):
    #     return str(self.id) + " " + str(self.tipo)
