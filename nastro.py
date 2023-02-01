from direzione import Direzione

class Nastro:
    def __init__(self, parola, alfabeto):
        self.alfabeto = alfabeto #+ "#"
        self.posizione_testa = 0
        self.__init_nastro(parola)

    # Per stampare le clssi per debuggare/capire
    # def __str__(self):
    #     return ''.join(self._nastro)

    def __init_nastro(self, parola):
        nastro = ""
        #for carattere in (c for c in parola if c in self.alfabeto):
        for carattere in parola:
            if carattere in self.alfabeto:
                nastro += carattere
        # nastro += "#"
        self._nastro = list(nastro)

    def scrivi(self, carattere):
        if self.posizione_testa < 0 or carattere not in self.alfabeto:
            return
        self._nastro[self.posizione_testa] = carattere
        # indice_ultimo_elemento= len(self._nastro) - 1
        # if self.posizione_testa == indice_ultimo_elemento:
        #     self._nastro += '#'

    def leggi(self):
        if self.posizione_testa < 0 or self.posizione_testa > len(self._nastro) - 1:
            raise Exeption('Provando a leggere carattere in posizione non valida: ' + self.posizione_testa)
        return self._nastro[self.posizione_testa]

    def get_nastro(self):
        self._rimuovere_cancelletti_finali()
        return ''.join(self._nastro) # Join all items in a tuple into a string, using a hash character as separator. Quindi nel nostro caso mettiamo insieme tutti i caratteri nel nastro, separandoli con il carattere vuoto ''

    def muovere_testa(self, direzione):
        if direzione == Direzione.Destra:
            self.posizione_testa += 1
        elif direzione == Direzione.Sinistra:
            self.posizione_testa -= 1
        # Questi due if penso che siano più per "errore", al momento non mi viene in mento un motivo del perché la testa dovrebbe essere più lunga della lunghezza del nastro o più piccolo di 0
        # if self.posizione_testa > len(self._nastro) - 1:
        #     self._nastro += "#"
        if self.posizione_testa < 0:
            self.posizione_testa = 0

    def get_lunghezza(self):
        return len(self._nastro)

# vedere se lo riesco a fare senza dover mettere questi cancelletti a caso
    def _rimuovere_cancelletti_finali(self):
        for i in range(len(self._nastro)-1, 1, -1): # range(start, stop, step) quindi iniziamo dalla fine del nastro e ci fermiamo all'indice 1, muovendoci decrescendo
            if self._nastro[i] == "#" and self._nastro[i-1] == "#":
                del self._nastro[-1:] # qui cancelliamo solo l'ultimo elemento della lista, se non ti ricordi, guarda qua:  https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/ (del è una parola chiave di python per cancellare oggetti)
            else:
                break
