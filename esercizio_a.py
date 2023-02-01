from macchina_di_turing import MacchinaDiTuring
from stato import Stato, TipoStato
from transizione import Transizione
from direzione import Direzione
from nastro import Nastro

# Dobbiamo modificare leggermente il testo dell'esercizio per riconoscere l'inizio del nastro
nastro = Nastro("$|||****", "|*$")
stati = [
    Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Nullo),
    Stato("s2", TipoStato.Nullo),
    Stato("s3", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]
transizioni = [
    Transizione("s0", "$", "s1", "$", Direzione.Destra),
    Transizione("s1", "|", "s1", "|", Direzione.Destra),
    Transizione("s1", "*", "s2", "|", Direzione.Destra),
    Transizione("s2", "*", "s3", "|", Direzione.Sinistra),
    Transizione("s3", "|", "s3", "|", Direzione.Sinistra),
    Transizione("s3", "$", "sf", "$", Direzione.Destra)
]

mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
