def somma_pari_ricorsiva(lista):
    if len(lista) == 0:
        return 0
    else:
        primo_numero = lista[0]
        lista_restante = lista[1:]
        if primo_numero % 2 == 0:
           return primo_numero + somma_pari_ricorsiva(lista_restante)
        else:
            return somma_pari_ricorsiva(lista_restante)

lista_numeri = [1, 34, 5, 67, 78, 24, 34, 9]
print(somma_pari_ricorsiva(lista_numeri))
