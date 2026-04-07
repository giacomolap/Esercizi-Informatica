def verifica_scacchiera(matrice):
    if len(matrice) == 0:
        return False
    if len(matrice) != len(matrice[0]):
        raise ValueError("Matrice non quadrata")
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            valore = matrice[i][j]
            somma_indici = i + j
            if somma_indici % 2 == 0 and valore % 2 != 0:
                return False
            if somma_indici % 2 != 0 and valore % 2 == 0:
                return False
    return True

M_corretta = [
    [2, 3],
    [5, 8]
]
M_sbagliata = [
    [2, 4],
    [5, 8]
]
print("Test 1 (deve essere True):", verifica_scacchiera(M_corretta))
print("Test 2 (deve essere False):", verifica_scacchiera(M_sbagliata))
