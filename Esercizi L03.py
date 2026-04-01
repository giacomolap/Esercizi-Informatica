# Esercizio 1 

def ripulisci_testo(ShesaRainbow):
    testo_ripulito = set()
    parole_escluse = [";;", "the", "a", "you", "she", "she's", "in", "her", "oh", "of", "and", "so"]
    for parola in ShesaRainbow.split():
         if parola not in parole_escluse:
            testo_ripulito.add(parola)
    return testo_ripulito

ShesaRainbow = "she comes in colours everywhere ;; she combs her hair ;; she's like a rainbow ;; coming colours in the air ;; oh everywhere ;; she comes in colours ;; she comes in colours everywhere ;; she combs her hair ;; she's like a rainbow ;; coming colours in the air ;; oh everywhere ;; she comes in colours ;; have you seen her dressed in blue ;; see the sky in front of you ;; and her face is like a sail ;; speck of white so fair and pale ;; have you seen a lady fairer ;; she comes in colours everywhere ;; she combs her hair ;; she's like a rainbow ;; coming colours in the air ;; oh everywhere ;; she comes in colours ;; have you seen her all in gold ;; like a queen in days of old ;; she shoots her colours all around ;; like a sunset going down ;; have you seen a lady fairer ;; she comes in colours everywhere ;; she combs her hair ;; she's like a rainbow ;; coming colours in the air ;; oh everywhere ;; she comes in colours ;; she's like a rainbow ;; coming colours in the air ;; oh everywhere ;; she comes in colours"
print(ripulisci_testo(ShesaRainbow))

# Esercizio 2 tramite ciclo for e ciclo if annidato

def quanti_colori(insieme_parole):
    n = 0
    lista_parole = ["colours", "rainbow", "white", "blue", "gold", "pale", "red", "green"]
    for parola in insieme_parole:
        if parola in lista_parole:
            n = n + 1
    return n

print(quanti_colori(ripulisci_testo(ShesaRainbow)))

# Esercizio 2 con intersezione di insiemi

def quanti_colori(insieme_parole):
    lista_parole = ["colours", "rainbow", "white", "blue", "gold", "pale", "red", "green"]
    parole_in_comune = insieme_parole.intersection(set(lista_parole))
    return len(parole_in_comune)

print(quanti_colori(ripulisci_testo(ShesaRainbow)))

# Esercizio 3

def conta_parole(stringa):
    un_dizionario = dict()
    n = 0
    parole_stringa = stringa.split()
    parole_da_escludere = [";;", "the", "a", "you", "she", "she's", "in", "her", "oh", "of", "and", "so", "i", "un"]
    for parole in parole_stringa:
        if parole not in parole_da_escludere:
            if parole in un_dizionario:
                un_dizionario[parole] = un_dizionario[parole] + 1
            else:
                un_dizionario[parole] = 1
    return un_dizionario
            
print(conta_parole(ShesaRainbow))     

