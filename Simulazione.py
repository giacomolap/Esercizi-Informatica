def crea_lista(stringa):
    listaNumeri = []
    while True:
        risposta = input(stringa)
        if risposta == "fine":
            break
        else:
            numero = int(risposta)
            listaNumeri.append(numero)       
    return listaNumeri

mia_lista = crea_lista("Scegli un numero da 0 a 9 o scrivi \"fine\" per terminare: ")
print("La lista generata è: ", mia_lista)

def somma_ricorsiva(listaDiNumeri):
    if len(listaDiNumeri) == 0:
        return 0
    else:
        primo_elemento = listaDiNumeri[0]
        resto_della_lista = listaDiNumeri[1:]
        return primo_elemento + somma_ricorsiva(resto_della_lista)
print("La somma degli elementi della lista é: " + str(somma_ricorsiva(mia_lista)))  
         
