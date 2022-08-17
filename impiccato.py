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
# lettere = [i for i in "cobais"]
random.shuffle(lettere)
ipotesi = ''.join(lettere)
parola = "ciao"
alfabeto = "abcdefghilmnopqrstuvzx@|-*"
input = ipotesi+"|"+"@@@@@@|"+parola+"|"




nastro = Nastro(input, alfabeto)
stati = [
    Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Nullo),
    Stato("s3", TipoStato.Nullo),
    Stato("s4", TipoStato.Nullo),
    Stato("s6", TipoStato.Nullo),
    Stato("sf", TipoStato.Finale)
]

stati_parola = [Stato("s"+i, TipoStato.Nullo) for i in parola]

stati += stati_parola

# transizioni = [
#     Transizione("s0", "$", "s1", "$", Direzione.Destra),
#     Transizione("s2", "|", "s2", "|", Direzione.Destra),
#     Transizione("s2", "@", "s2", "@", Direzione.Destra),
#     Transizione("s2", "#", "s3", "#", Direzione.Sinistra),
#     Transizione("s3", "$", "s1", "$", Direzione.Destra),
#     Transizione("s3", "*", "s1", "*", Direzione.Destra),
#     Transizione("s4", "|", "s4", "|", Direzione.Destra),
#     Transizione("s4", "x", "s5", "x", Direzione.Destra),
#     Transizione("s5", "@", "s3", "x", Direzione.Sinistra),
#     Transizione("s5", "x", "s5", "x", Direzione.Destra),
#     Transizione("s5", "|", "sf", "|", Direzione.Neutrale),
#     Transizione("s1", "|", "sf", "|", Direzione.Neutrale)
# ]

transizioni = [
    Transizione("s0", "$", "s1", "$", Direzione.Destra),
    Transizione("s1", "|", "sf", "|", Direzione.Neutrale),
    Transizione("s3", "*", "s1", "*", Direzione.Destra),
    Transizione("s4", "@", "s3", "x", Direzione.Sinistra),
    Transizione("s4", "x", "s6", "x", Direzione.Destra),
    Transizione("s6", "x", "s6", "x", Direzione.Destra),
    Transizione("s6", "@", "s3", "x", Direzione.Sinistra),
    Transizione("s6", "|", "sf", "|", Direzione.Neutrale)

]

lettere_sbagliate = alfabeto
for i in parola :
    lettere_sbagliate=lettere_sbagliate.replace(i,"")

# giuste_4= [Transizione("s"+i, j, "s"+i, j, Direzione.Destra) for i in parola and j in alfabeto-i]

scorri = []

for i in parola:
    for j in alfabeto:
        if j != i and j != "#":
            scorri.append(Transizione("s"+i, j, "s"+i, j, Direzione.Destra))

giuste= [Transizione("s1", i, "s"+i, "*", Direzione.Destra) for i in parola]
giuste_2= [Transizione("s"+i, i, "s"+i, "-", Direzione.Destra) for i in parola]
giuste_3= [Transizione("s"+i, "#", "s3", "#", Direzione.Sinistra) for i in parola]
sbagliate = [Transizione("s1", i, "s4", "*", Direzione.Destra) for i in lettere_sbagliate]
raggiungi_vita = [Transizione("s4", i, "s4", i, Direzione.Destra) for i in [j for j in alfabeto if j != "@" or j != "x"]]
torna_inizio = [Transizione("s3", i, "s3", i, Direzione.Sinistra) for i in [j for j in alfabeto if j != "*"]] #qui voglio che valga per tutti tranne che per *



transizioni = transizioni + scorri + giuste + giuste_2 + giuste_3 + sbagliate + raggiungi_vita + torna_inizio
mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
