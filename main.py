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


