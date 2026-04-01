def studenti_meritevoli(registro, media_soglia):
    promossi = []
    for studente in registro:
        nome_studente = studente["nome"]
        lista_voti = studente["voti"]
        if len(lista_voti) > 0:
            media = sum(lista_voti)/len(lista_voti)
            if media >= media_soglia:
                promossi.append(nome_studente)
    return promossi      
            
            
def test_studenti_meritevoli(registro, media_soglia, val_atteso):
    risultato = studenti_meritevoli(registro, media_soglia)
    if risultato == val_atteso:
        return True
    else:
        return False
                            

registro = [{"nome": "Giacomo", "voti": [24, 28, 27]},
    {"nome": "Anna", "voti": [30, 30, 29]},
    {"nome": "Marco", "voti": [23, 18, 21]}, 
    {"nome": "Lucia", "voti": [18, 30, 25]},
    {"nome": "Fantasma", "voti": []}]

print(studenti_meritevoli(registro, 27))
print(test_studenti_meritevoli(registro, 27, ["Anna"]))
            
       
    
    
