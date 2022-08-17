from macchina_di_turing import MacchinaDiTuring
from stato import Stato, TipoStato
from transizione import Transizione
from direzione import Direzione
from nastro import Nastro

nastro = Nastro("|||", "|")
stati = [
    Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]
transizioni = [
    Transizione("s0", "$", "s1", "$", Direzione.Destra),
    Transizione("s1", "|", "s1", "|", Direzione.Destra),
    Transizione("s1", "#", "sf", "|", Direzione.Neutrale)
]

mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
