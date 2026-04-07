def is_palindroma(lista):
    if len(lista) <= 1:
        return True
    if lista[0] != lista[-1]:
        return False
    else:
        return is_palindroma(lista[1:-1])
                             
print(is_palindroma([1, 2, 3, 2, 1]))
print(is_palindroma([1, 2, 3, 4, 5])) 
print(is_palindroma(["a", "n", "n", "a"]))
