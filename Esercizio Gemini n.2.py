def analizza_risultati(registro):
    if len(registro) == 0:
        raise ValueError("Registro vuoto, impossibile procedere")
    else:
        studenti_top = []
        for nome, voto in registro.items():
            if voto >= 27:
                studenti_top.append(nome)
    return studenti_top

voti_appello = {}
print(analizza_risultati(voti_appello))
