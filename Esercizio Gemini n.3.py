def conta_carattere(stringa, carattere):
    if len(carattere) != 1:
        raise ValueError("Input non valido: inserire un singolo carattere")         
    if len(stringa) == 0:
        return 0
    if stringa[0] == carattere:
        return 1 + conta_carattere(stringa[1:], carattere)
    else:
        return conta_carattere(stringa[1:], carattere)

print(conta_carattere("informatica", "a"))  
print(conta_carattere("python", "z"))      
