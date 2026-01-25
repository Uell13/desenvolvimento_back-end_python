numero = int(input('Escolha um número inteiro: '))
calculo = numero % 2
if calculo != 1:
    print(f'O número escolhido "{numero}" é par!')
else:
    print(f'O número escolhido "{numero}" é impar!')