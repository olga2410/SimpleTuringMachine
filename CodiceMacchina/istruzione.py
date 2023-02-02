
class Istruzione:
    def __init__(self, stato_corrente, carattere_corrente, nuovo_stato, nuovo_carattere, direzione):
        self.stato_corrente = stato_corrente
        self.carattere_corrente = carattere_corrente
        self.nuovo_stato = nuovo_stato
        self.nuovo_carattere = nuovo_carattere
        self.direzione = direzione

    # Per stampare le clssi per debuggare/capire
    def __str__(self):
        return str(self.stato_corrente) + " " + str(self.carattere_corrente) + " " + str(self.nuovo_stato) + " " + str(self.nuovo_carattere) + " " + str(self.direzione)
