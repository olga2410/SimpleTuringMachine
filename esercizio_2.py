from macchina_di_turing import MacchinaDiTuring
from stato import Stato, TipoStato
from transizione import Transizione
from direzione import Direzione
from nastro import Nastro

#Anche questo modificato per indicare l'inizio del nastro
nastro = Nastro("$10**", "10*$")
stati = [
    Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Nullo),
    Stato("s2", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]
transizioni = [
    Transizione("s0", "$", "s1", "$", Direzione.Destra),
    Transizione("s1", "0", "s1", "0", Direzione.Destra),
    Transizione("s1", "1", "s1", "1", Direzione.Destra),
    Transizione("s1", "*", "s2", "0", Direzione.Sinistra),
    Transizione("s2", "0", "s2", "0", Direzione.Sinistra),
    Transizione("s2", "1", "s2", "1", Direzione.Sinistra),
    Transizione("s2", "$", "sf", "$", Direzione.Destra),


                
                            
]

mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
