apples = int(input('Quantas maçãs foram vendidas? '))
bananas = int(input('Quantas bananas foram vendidas? '))

if apples > bananas:
    print('As maçãs tiveram mais vendas.')
elif bananas > apples:
    print('As bananas tiveram mais vendas.')
else:
    print('As vendas de maçãs e bananas foram iguais.')