import os

renda_mensal_minima = 2000

os.system('cls' if os.name == 'nt' else 'clear')
print('------------------------------')
print('Análise de Empréstimo Bancário')
print('------------------------------\n')

renda_mensal = float(input('Digite sua renda mensal: R$ '))
if renda_mensal < renda_mensal_minima:
    print(f'\nSua renda mensal é inferior ao mínimo exigido de R$ {renda_mensal_minima:.2f}')
    print('Empréstimo negado.')
    exit()

valor_emprestimo = float(input('Digite o valor do empréstimo desejado: R$ '))

if valor_emprestimo > (renda_mensal * .3):
    print('\nEmpréstimo negado. O valor do empréstimo excede 30% da sua renda mensal.')
else:
    print('\nEmpréstimo aprovado!')