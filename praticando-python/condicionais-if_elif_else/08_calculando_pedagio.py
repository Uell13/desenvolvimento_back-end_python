import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_continue():
    input('Pressione ENTER para continuar...')

while True:

    limpar_terminal()
    print('------------------')
    print('Cálculo de Pedágio')
    print('------------------\n')
    
    print('Digite 0 para encerrar o programa.')
    distancia_percorrida = float(input('Digite a distância percorrida (em KM): '))

    print() # Linha em branco para melhor visualização
    if distancia_percorrida == 0:
        print('Encerrando o programa de cálculo de pedágio.')
        break
    elif 0 < distancia_percorrida <= 100:
        print(f'O valor do pedágio é R$10,00 para {distancia_percorrida:.2f} KM percorridos.')
        enter_continue()
    elif 100 < distancia_percorrida <= 200:
        print(f'O valor do pedágio é R$20,00 para {distancia_percorrida:.2f} KM percorridos.')
        enter_continue()
    elif distancia_percorrida > 200:
        print(f'O valor do pedágio é R$30,00 para {distancia_percorrida:.2f} KM percorridos.')
        enter_continue()
    else:
        print('Distância inválida.')
        enter_continue()
    
    continue
