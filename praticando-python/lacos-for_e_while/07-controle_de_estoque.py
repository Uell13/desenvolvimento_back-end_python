# Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".

estoque = 5

print() # Espaço em branco para melhor visualização
while estoque > 0:
    estoque -= 1 # Reduz o estoque a cada venda
    print(f'Venda realizada! Estoque restante: {estoque}')

print('Estoque esgotado.')
