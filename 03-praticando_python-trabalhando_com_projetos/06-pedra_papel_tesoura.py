'''
Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura.
O computador escolherá aleatoriamente uma opção.
O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.

Exemplo de entrada:
Escolha: pedra, papel ou tesoura? papel

Saída esperada:
Computador escolheu: pedra
Você venceu!

Caso o computador vença:
Computador escolheu: tesoura  
Você perdeu!

Caso o computador escolha a mesma opção que você:
Computador escolheu: papel 
Empate!
'''

import random
import os

OPCOES = (
    'pedra',
    'papel',
    'tesoura',
    # 'largato',
    # 'spock'
)
REGRA = {
    'pedra': 'tesoura',
    'tesoura': 'papel',
    'papel': 'largato',
    # 'largato': 'spock',
    # 'spock': 'pedra'
}

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def mostrar_titulo():
    print(f'--- {', '.join(OPCOES[:len(OPCOES)-1])+' ou '+OPCOES[len(OPCOES)-1]} ---')

def resposta_usuario() -> str:
    while True:
        escolha = input(f'Escolha: {', '.join(OPCOES[:len(OPCOES)-1])+' ou '+OPCOES[len(OPCOES)-1]}: ').lower().strip()
        if escolha in OPCOES:
            return escolha
        print(f'\nEntrada inválida!\n')

def pedra_papel_tesoura(usuario: str, computador: str) -> str:   
    if usuario == computador:
        return 'Empate!!'
    elif REGRA[usuario] == computador:
        return 'Você venceu!'
    else:
        return 'Você perdeu!'

def main():
    limpar_terminal()
    mostrar_titulo()
    escolha_usuario = resposta_usuario()
    escolha_computador = random.choice(OPCOES)
    
    print(f'\nSua escolha: {escolha_usuario}')
    print(f'Computador escolheu: {escolha_computador}')
    
    resultado = pedra_papel_tesoura(escolha_usuario, escolha_computador)
    print(f'Resultado: {resultado}')

if __name__ == '__main__':
    main()
