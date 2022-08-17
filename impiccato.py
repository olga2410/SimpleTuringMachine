from macchina_di_turing import MacchinaDiTuring
from stato import Stato, TipoStato
from transizione import Transizione
from direzione import Direzione
from nastro import Nastro
import random


# separatore = "|"
# vita = @
# Lista casuale di 21 lettere
lettere = [i for i in "abcdefghilmenopqrstuvz"]
random.shuffle(lettere)
ipotesi = ''.join(lettere)
parola = "ciao"
alfabeto = "abcdefghilmnopqrstuvzx@|-*"
input = ipotesi+"|"+"@@@@@@"+parola+"|"




nastro = Nastro(input, alfabeto)
stati = [
    Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Nullo),
    Stato("s2", TipoStato.Nullo),
    Stato("s3", TipoStato.Nullo),
    Stato("s4", TipoStato.Nullo),
    Stato("s5", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]
transizioni = [
    Transizione("s0", "$", "s1", "$", Direzione.Destra),
    Transizione("s2", "|", "s2", "|", Direzione.Destra),
    Transizione("s2", "@", "s2", "@", Direzione.Destra),
    Transizione("s2", "#", "s3", "#", Direzione.Sinistra),
    Transizione("s3", "$", "s1", "$", Direzione.Destra),
    Transizione("s3", "*", "s1", "*", Direzione.Destra),
    Transizione("s4", "|", "s4", "|", Direzione.Destra),
    Transizione("s4", "x", "s5", "x", Direzione.Destra),
    Transizione("s5", "@", "s3", "x", Direzione.Sinistra),
    Transizione("s5", "x", "s5", "x", Direzione.Destra),
    Transizione("s5", "|", "sf", "|", Direzione.Neutrale),
    Transizione("s1", "|", "sf", "|", Direzione.Neutrale)
]

lettere_sbagliate = alfabeto
for i in parola :
    lettere_sbagliate=lettere_sbagliate.replace(i,"")

giuste= [Transizione("s1", i, "s2", "*", Direzione.Destra) for i in parola]
sbagliate = [Transizione("s1", i, "s2", "*", Direzione.Destra) for i in lettere_sbagliate]
sostituzione =  [Transizione("s2", i, "s2", "-", Direzione.Destra) for i in parola]
torna_inizio = [Transizione("s3", i, "s3", i, Direzione.Sinistra) for i in alfabeto]

transizioni = transizioni + giuste + sbagliate + sostituzione + torna_inizio

mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
