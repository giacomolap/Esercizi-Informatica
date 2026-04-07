def calcola_voto_finale(lista_voti):
    if len(lista_voti) == 0:
        raise IndexError("La lista é vuota, si prega di inserire tre elementi")
    if len(lista_voti) != 3:
        raise ValueError("la lista non contiene esattamente tre elementi")
    votouno = lista_voti[0] 
    votodue = lista_voti[1] 
    vototre = lista_voti[2] 
    media_ponderata = (votouno + votodue + vototre * 2) / 4
    return media_ponderata

lista_voti = [26, 27, 25]
print(calcola_voto_finale(lista_voti))
