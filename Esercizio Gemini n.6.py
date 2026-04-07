def calcola_val_tot(magazzino):
    if len(magazzino) == 0:
        return 0.0
    else:
        valore_totale = 0.0
        for marca, dati_marca in magazzino.items():
            if len(dati_marca) == 2:
                quantita = dati_marca[0]
                prezzo = dati_marca[1]
                valore_totale = valore_totale + (quantita * prezzo)
        return valore_totale
                
scorte_magazzino = {
    "Sant'Anna": [100, 2.5],
    "Levissima": [50],         
    "Rocchetta": [200, 1.5],
    "San Benedetto": [0, 2.0, 5]
}
print(calcola_val_tot(scorte_magazzino))
