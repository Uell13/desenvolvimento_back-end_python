'''
Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta.
O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

Exemplo de entrada:
Digite o valor da conta: 120.00  
Digite a porcentagem de gorjeta: 10

Saída esperada:
Valor da gorjeta: R$ 12.00  
Total a pagar: R$ 132.00
'''

import os

def limpar_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def is_number(msg:str):
    while True:
        dado = input(msg).replace(',', '.')
        try:
            return float(dado)
        except ValueError:
            limpar_terminal()
            print('Erro! Você deve informar um valor válido.')

def is_valid(msg:str):
    while True:
        dado = input(msg).replace(',', '.')
        try:
            dado = float(dado)

            if not 0 <= dado <= 100:
                limpar_terminal()
                print('A porcentagem deve ser entre 0 e 100')
                continue

            return dado
        except ValueError:
            limpar_terminal()
            print('Erro! Você deve informar um valor válido.')

def conta_total(conta, porcentagem):
    conta_detalhada = {}
    conta_detalhada['percentual'] = porcentagem / 100
    conta_detalhada['valor_conta'] = conta
    conta_detalhada['valor_gorjeta'] = conta * conta_detalhada['percentual']
    conta_detalhada['total'] = conta_detalhada['valor_conta'] + conta_detalhada['valor_gorjeta']
    return conta_detalhada

def main():
    while True:
        limpar_terminal()
        conta = is_number('Digite o valor da conta: ')
        porcentagem = is_valid('Digite a porcentagem de gorjeta: ')

        limpar_terminal()
        print()
        print('-' * 30)
        resultado = conta_total(conta, porcentagem)
        print(f'''Porcentagem aplicada: {resultado['percentual']*100}%\n
Valor da conta: R$ {resultado['valor_conta']:.2f}
Valor da gorjeta: R$ {resultado['valor_gorjeta']:.2f}
Total a pagar: R$ {resultado['total']:.2f}'''.replace('.', ','))
        print('-' * 30)
        print()
        
        print('Digite "nao" para finalizar o programa ou')
        if input('Pressione Enter para continuar...') == 'nao':
            break

if __name__ == '__main__':
    main()
