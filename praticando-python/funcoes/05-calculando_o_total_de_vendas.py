'''
Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia.
As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
'''


'''
A Estrutura do map()
1. Uma função: a transformação que você quer aplicar.
2. Um iterável: os dados originais.
'''
def somar_vendas(lista):
    return sum(map(float, lista))

valores_vendas = input('Digite os valores das vendas (separando por espaços): ').split()

soma = somar_vendas(valores_vendas)
print(f'O total de vendas foi: R${soma:.2f}')
