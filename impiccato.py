from CodiceMacchina.macchina_di_turing import MacchinaDiTuring
from CodiceMacchina.stato import Stato, TipoStato
from CodiceMacchina.istruzione import Istruzione
from CodiceMacchina.direzione import Direzione
from CodiceMacchina.nastro import Nastro
import random


# separatore = "|"
# vita = @
# Lista casuale di 21 lettere
lettere = [i for i in "abcdefghilmnopqrstuvz"]
# lettere = [i for i in "cobaisz"]
random.shuffle(lettere)
ipotesi = ''.join(lettere)
parola = "ciao"
alfabeto = "abcdefghilmnopqrstuvzx@|-*"+"$#"
input = "$"+ipotesi+"|"+"@@@@@@|"+parola+"#"




nastro = Nastro(input, alfabeto)
stati = [
    Stato("s0", TipoStato.Iniziale),
    Stato("s1", TipoStato.Nullo),
    Stato("s3", TipoStato.Nullo),
    Stato("s4", TipoStato.Nullo),
    Stato("s6", TipoStato.Nullo),
    Stato("s5", TipoStato.Nullo),
    Stato("sfin", TipoStato.Finale)
] + [Stato("s"+i, TipoStato.Nullo) for i in parola] + \
    [Stato("s2"+i, TipoStato.Nullo) for i in parola] + \
    [Stato("s3"+i, TipoStato.Nullo) for i in parola]


lettere_sbagliate = alfabeto
for i in parola :
    lettere_sbagliate=lettere_sbagliate.replace(i,"")

scorri = []
for i in parola:
    for j in alfabeto:
        if j != i and j != "#" and j != "-":
            scorri.append(Istruzione("s"+i, j, "s"+i, j, Direzione.Destra))


scorri_vittoria = []
for i in parola:
    for j in parola:
        if i != j:
            scorri_vittoria.append(Istruzione("s2"+i, j, "s3"+i, j, Direzione.Destra))

scorri_vittoria_3 = []
for i in parola:
    for j in alfabeto:
        if i != j:
            scorri_vittoria_3.append(Istruzione("s3"+i, j, "s3"+i, j, Direzione.Destra))


transizioni = [
    Istruzione("s0", "$", "s1", "$", Direzione.Destra),
    Istruzione("s1", "|", "sfin", "|", Direzione.Neutrale),
    Istruzione("s3", "*", "s1", "*", Direzione.Destra),
    Istruzione("s4", "@", "s5", "x", Direzione.Destra),
    Istruzione("s4", "x", "s6", "x", Direzione.Destra),
    Istruzione("s6", "x", "s6", "x", Direzione.Destra),
    Istruzione("s6", "@", "s5", "x", Direzione.Destra),
    Istruzione("s6", "|", "sfin", "|", Direzione.Neutrale),
    Istruzione("s5", "-", "s5", "-", Direzione.Destra),
    Istruzione("s5", "#", "sfin", "#", Direzione.Neutrale),
    Istruzione("s5", "@", "s5", "@", Direzione.Destra),
    Istruzione("s5", "|", "s5", "|", Direzione.Destra)

] + [Istruzione("s1", i, "s"+i, "*", Direzione.Destra) for i in parola] + \
    [Istruzione("s"+i, i, "s"+i, "-", Direzione.Destra) for i in parola] + \
    [Istruzione("s"+i, "#", "s3", "#", Direzione.Sinistra) for i in parola] + \
    [Istruzione("s1", i, "s4", "*", Direzione.Destra) for i in lettere_sbagliate] + \
    [Istruzione("s4", i, "s4", i, Direzione.Destra) for i in [j for j in alfabeto if j != "@" and j != "x"]] + \
    [Istruzione("s3", i, "s3", i, Direzione.Sinistra) for i in [j for j in alfabeto if j != "*"]] + \
    [Istruzione("s5", i, "s3", i, Direzione.Sinistra) for i in parola] + \
    [Istruzione("s2"+i, i, "s2"+i, "-", Direzione.Destra) for i in parola] + \
    [Istruzione("s2"+i, "-", "s2"+i, "-", Direzione.Destra) for i in parola] + \
    [Istruzione("s"+i, "-", "s2"+i, "-", Direzione.Destra) for i in parola] + \
    [Istruzione("s2"+i, "#", "sfin", "#", Direzione.Neutrale) for i in parola] + \
    [Istruzione("s3"+i, i, "s3"+i, "-", Direzione.Destra) for i in parola] + \
    [Istruzione("s3"+i, "#", "s3", "#", Direzione.Sinistra) for i in parola]


transizioni = transizioni + scorri + scorri_vittoria + scorri_vittoria_3


mt = MacchinaDiTuring(stati, transizioni, nastro)
mt.processa()
print(mt.get_nastro())
