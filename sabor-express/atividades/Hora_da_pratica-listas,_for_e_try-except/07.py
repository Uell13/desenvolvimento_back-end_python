notas = [8.5, 7.0, 9.0, 6.5, 10.0]
soma = 0
try:
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    print(f'A média das notas é: {media}')
except ZeroDivisionError:
    print('A lista de notas está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'Ocorreu um erro ao calcular a média: {e}')