from .direzione import Direzione

class Nastro:
    def __init__(self, input, alfabeto, posizione_testa=0):
        self.alfabeto = alfabeto
        self.posizione_testa = posizione_testa
        self._nastro = list(input)

    # Per stampare le clssi per debuggare/capire
    # def __str__(self):
    #     return ''.join(self._nastro)


    def scrivi(self, carattere):
        if self.posizione_testa < 0 or carattere not in self.alfabeto:
            return
        self._nastro[self.posizione_testa] = carattere


    def leggi(self):
        if self.posizione_testa < 0 or self.posizione_testa > len(self._nastro) - 1:
            raise OverflowError('Provando a leggere carattere in posizione non valida: ' + self.posizione_testa)
        return self._nastro[self.posizione_testa]

    def get_nastro(self):
        return ''.join(self._nastro) 
        
    def muovere_testa(self, direzione):
        if direzione == Direzione.Destra:
            self.posizione_testa += 1
        elif direzione == Direzione.Sinistra:
            self.posizione_testa -= 1
        if self.posizione_testa < 0:
            self.posizione_testa = 0

    def get_lunghezza(self):
        return len(self._nastro)


