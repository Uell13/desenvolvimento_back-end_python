'''
Crie um programa que junte duas listas e exiba o resultado no formato produto: preço
'''

import os

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')
def exibir_titulo():
    titulo = 'DESAFIO 07 | Juntando listas de produtos | Alura'
    print('-' * len(titulo))
    print(titulo)
    print('-' * len(titulo))
    print()
def enter_continue():
    return input('Pressione a tecla Enter para continuar...')

while True:
    try:
        limpar_terminal()
        exibir_titulo()
        produtos = [p.strip() for p in input('Digite os produtos separados por vírgula: ').split(',') if p.strip()]
        if not produtos or produtos == ['']:
            print()
            print('Você deve informar pelo menos um produto!')
            enter_continue()
            continue
        break
    except:
        print()
        print('Caiu aqui!')
        enter_continue()

while True:
    try:
        limpar_terminal()
        exibir_titulo()
        print(f'Produtos informados: {' - '.join(produtos)}')
        precos = [float(p.strip()) for p in input('Digite os preços separados por vírgula: ').split(',') if p.strip()]
        if not precos or precos == ['']:
            print()
            print('Erro! Você deve informar os preços do produtos listados.')
            enter_continue()
            continue
        if len(produtos) != len(precos):
            print()
            print('A quantidade de preço dos produtos deve ser a mesma dos produtos listados.')
            print(f'Você passou {len(produtos)} produtos, e agora deve passar {len(produtos)} preços para esses produtos!')
            enter_continue()
            continue
        break
    except:
        print()
        print('Você deve digitar apenas números nesse campo!')
        enter_continue()

limpar_terminal()
exibir_titulo()
print('RESULTADO')
print()
print(f'{'PRODUTOS'.ljust(10)} | PREÇOS')
for produto, preco in zip(produtos, precos):
    print(f'{produto.ljust(10)} | R$ {preco:.2f}'.replace('.', ','))
