"""
Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes.
Elas querem um programa que mostre:

Quais itens apareceram nas duas listas
Quais foram exclusivos de Laura
Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações.
"""

lista_laura = set(['leite', 'pão', 'café', 'açúcar'])
lista_ana = set(['pão', 'café', 'biscoito', 'chocolate'])

comum = lista_ana & lista_laura
nova_lista_ana = lista_ana - lista_laura
nova_lista_laura = lista_laura - lista_ana

print(f'Itens em ambas as listas: {', '.join(comum)}',
      f'\nItens exclusivos de Ana: {', '.join(nova_lista_ana)}',
      f'\nItens exclusivos de Laura: {', '.join(nova_lista_laura)}')
