minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0
for numero in minha_lista:
    if numero % 2 == 1:
        soma += numero

print("A soma dos números ímpares na lista é:", soma)