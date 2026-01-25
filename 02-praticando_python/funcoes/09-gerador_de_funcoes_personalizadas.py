'''
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

Exemplo de entrada:
Digite a porcentagem de desconto: 10
Digite o valor da compra: 200

Saída esperada:
Preço final com desconto: 180.0
'''

def is_number(mensagem_input):
    while True:
        numero = input(mensagem_input).strip()
        try:
            return float(numero)
        except ValueError:
            print('Erro! Dado inválido. Você deve fornecer um número.')

def aplicar_desconto(valor, porcentagem):
    return valor - (valor * (porcentagem / 100))

porcentagem = is_number('Digite a porcentagem de desconto: ')
valor_compra = is_number('Digite o valor da compra: ')

valor_final = aplicar_desconto(valor_compra, porcentagem)
print(f'Preço final com desconto: R$ {valor_final:.2f}'.replace('.', ','))
