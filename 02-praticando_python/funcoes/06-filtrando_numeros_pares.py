'''
Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
'''

numeros = input('Digite os números separados por espaço: ').split()

'''
A função filter() recebe dois argumentos principais:
Uma função: que define a regra de filtragem (deve retornar True ou False).
Um iterável: o conjunto de dados que você quer filtrar (uma lista, por exemplo).
O filter() aplica a função a cada item do iterável. Se a função retornar True, o item é mantido; se retornar False, ele é descartado.
** A função não retorna uma lista direto por isso usei o list() para transformar o que recebemos em uma lista
'''
numeros_pares = list(filter(lambda x: x % 2 == 0, map(int, numeros)))

print(numeros_pares)
