from CodiceMacchina.macchina_di_turing import MacchinaDiTuring
from CodiceMacchina.stato import Stato, TipoStato
from CodiceMacchina.istruzione import Istruzione
from CodiceMacchina.direzione import Direzione
from CodiceMacchina.nastro import Nastro

nastro = Nastro("|||*****", "|*")
stati = [
    # Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Iniziale),
    Stato("s2", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]
transizioni = [
    Istruzione("s1", "|", "s1", "|", Direzione.Destra),
    Istruzione("s1", "*", "s2", "|", Direzione.Destra),
    Istruzione("s2", "*", "sf", "|", Direzione.Neutrale)
]

mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
