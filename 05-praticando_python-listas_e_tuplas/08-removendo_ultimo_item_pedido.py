"""
Paulo está criando uma lista de pedidos para a lanchonete.
Ele já tem todos os pedidos, mas percebeu que o último foi inserido por engano e precisa removê-lo.

Diante deste problema, ajude Paulo criando um programa que automatize essa operação, permitindo listar os pedidos e remover o último item automaticamente.

Exemplo de Entrada:
Pedidos feitos (separados por vírgula): Sanduíche, Suco, Sobremesa

Saída esperada:
Pedidos finais: ['Sanduíche', 'Suco']
"""

pedidos = [p.strip() for p in input('Pedidos feitos (separados por vírgula): ').split(',') if p.strip()]
pedidos.pop(-1)
print(f'Pedidos finais: {pedidos}')
