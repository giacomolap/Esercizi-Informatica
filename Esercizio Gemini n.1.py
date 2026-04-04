def massimo_ricorsivo(lista_di_numeri):
    if len(lista_di_numeri) == 0:
        return "La lista è vuota, non esiste massimo" 
   
    if len(lista_di_numeri) == 1:
        return lista_di_numeri[0]
    else:
        primo_elemento = lista_di_numeri[0]
        resto_della_lista = lista_di_numeri[1:]
        massimo_del_resto = massimo_ricorsivo(resto_della_lista)
        if primo_elemento > massimo_del_resto:
            return primo_elemento
        else:
            return massimo_del_resto
            

lista_di_numeri = []
print(massimo_ricorsivo(lista_di_numeri))
           
