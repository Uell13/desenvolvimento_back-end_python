'''
Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
'''

def contador_caracteres(palavra):
    caracteres = 0
    for _ in palavra:
        caracteres += 1
    return caracteres

texto = input('Digite uma palavra: ')
contador = contador_caracteres(texto)

print(f'Quantidade de caracteres: {contador}')
