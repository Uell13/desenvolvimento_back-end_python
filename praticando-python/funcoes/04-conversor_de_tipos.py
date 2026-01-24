'''
Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings.
No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:
'''

def converte_para_inteiro(lista):
    '''
    Recebe uma lista de números de telefones do tipo str
    e retorna uma nova lista com os números convertidos para o tipo int
    '''
    return [int(telefone) for telefone in lista]

def verifica_lista(lista):
    '''
    Percorre a lista de números de telefone fornecida e verifica se
    existe algum valor com o tipo str
    retorna uma mensagem(str) se encontrar um valor do tipo str
    '''
    for numero in lista:
        if not isinstance(numero, int):
            return 'Encontrei valores do tipo string armazenados na lista.'
    return 'Todos os números foram convertidos corretamente!'

telefones = [
    "11987654321",
    "21912345678",
    "31987654321",
    "11911223344"
]

lista = converte_para_inteiro(telefones)
print(verifica_lista(lista))
