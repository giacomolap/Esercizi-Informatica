def cerca_anomalie(matrice, soglia):
    if len(matrice) == 0:
        raise ValueError("Dati insuffcienti")
    anomalie = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] > soglia:
                anomalie.append((i,j))
    return anomalie
                                
temperature = [
    [20, 23, 26, 27, 21, 21, 29],
    [30, 31, 29, 30, 28, 27, 32],
    [17, 18, 19, 16, 20, 22, 20]
]
soglia_allarme = 30
print(cerca_anomalie(temperature, soglia_allarme))                               
