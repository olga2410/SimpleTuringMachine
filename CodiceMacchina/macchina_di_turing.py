from .stato import TipoStato
import time

# Le due righe seguenti sono per far funzionare la stampa del log su windows
import os
os.system("")

class MacchinaDiTuring:
    def __init__(self, stati, transizioni, nastro):
        self.stati = stati
        self.stato_iniziale= self.get_stato_iniziale()
        self.transizioni = transizioni
        self.nastro = nastro

    def get_nastro(self):
        return self.nastro.get_nastro()

    def get_stato_iniziale(self):
        return next(stato for stato in self.stati if stato.tipo == TipoStato.Iniziale)

    def processa(self):
        stato_corrente = self.stato_iniziale
        passo = 0
        self._log_processo(passo)

        while stato_corrente.tipo != TipoStato.Finale:
            carattere_corrente = self.nastro.leggi()
            id_stato = stato_corrente.id
            transizione = next(t for t in self.transizioni if t.stato_corrente == id_stato and t.carattere_corrente == carattere_corrente)
            print(transizione)
            stato_corrente = next(stato for stato in self.stati if stato.id == transizione.nuovo_stato)
            print(stato_corrente)
            self.nastro.scrivi(transizione.nuovo_carattere)
            self.nastro.muovere_testa(transizione.direzione)

            passo +=1
            self._log_processo(passo)

    def _log_processo(self, passo):
        print("\nNastro dopo {0} passi".format(passo))
        print("[", end='')

        for i in range(0, self.nastro.get_lunghezza()):
            if self.nastro.posizione_testa == i:
                print("\033[4m" + self.nastro._nastro[i] + "\033[0m", end="")
            else:
                print(self.nastro._nastro[i], end="")

        print("]")
        # time.sleep(1.0)
        os.system('cls')
