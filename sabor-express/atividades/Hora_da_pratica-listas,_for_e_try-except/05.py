data_numero = input('Digite um número inteiro para ver a sua tabuada: ')
try:
    numero = int(data_numero)
    print(f'Tabuada do {numero}:')
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
except:
    print('Por favor, digite um número inteiro válido.')