# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.
# Exemplo de entrada:
# Digite um texto: A linguagem Python é muito versátil.
# Saída esperada:
# O texto contém 13 vogais.

def contar_vogais(texto:str):
    vogais = set('aáàãeéêiíoóôuú')
    return sum(1 for letra in texto.lower() if letra in vogais)

def main():
    texto = input('Digite um texto: ')
    print(contar_vogais(texto))

if __name__ == '__main__':
    main()
