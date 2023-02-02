from CodiceMacchina.macchina_di_turing import MacchinaDiTuring
from CodiceMacchina.stato import Stato, TipoStato
from CodiceMacchina.istruzione import Istruzione
from CodiceMacchina.direzione import Direzione
from CodiceMacchina.nastro import Nastro

#Anche questo modificato per indicare l'inizio del nastro
nastro = Nastro("*10**", "10*$", 1)
stati = [
    # Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Iniziale),
    Stato("s2", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]
transizioni = [
    # Transizione("s0", "$", "s1", "$", Direzione.Destra),
    Istruzione("s1", "0", "s1", "0", Direzione.Destra),
    Istruzione("s1", "1", "s1", "1", Direzione.Destra),
    Istruzione("s1", "*", "s2", "0", Direzione.Sinistra),
    Istruzione("s2", "0", "s2", "0", Direzione.Sinistra),
    Istruzione("s2", "1", "s2", "1", Direzione.Sinistra),
    Istruzione("s2", "*", "sf", "*", Direzione.Destra),


                
                            
]

mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
