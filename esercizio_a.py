from CodiceMacchina.macchina_di_turing import MacchinaDiTuring
from CodiceMacchina.stato import Stato, TipoStato
from CodiceMacchina.istruzione import Istruzione
from CodiceMacchina.direzione import Direzione
from CodiceMacchina.nastro import Nastro

nastro = Nastro("*|||****", "|*$", 1)
stati = [
    Stato("s1", TipoStato.Iniziale),
    Stato("s2", TipoStato.Nullo),
    Stato("s3", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]
transizioni = [
    Istruzione("s1", "|", "s1", "|", Direzione.Destra),
    Istruzione("s1", "*", "s2", "|", Direzione.Destra),
    Istruzione("s2", "*", "s3", "|", Direzione.Sinistra),
    Istruzione("s3", "|", "s3", "|", Direzione.Sinistra),
    Istruzione("s3", "*", "sf", "*", Direzione.Destra)
]

mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
