# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras.
# Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

# Exemplo de entrada:
# Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais

# Saída esperada:
# Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais

# Se nenhum palavra longa for encontrada:
# Nenhuma palavra longa foi encontrada no texto.

def filtrar_palavras_longas(texto: str, limite: int = 10) -> list[str]:
    '''Retorna uma lista com as palavras longas encontradas'''
    return [p for p in texto.split() if len(p) >= limite]

def main():
    entrada = input('Digite um texto: ').strip()

    if not entrada:
        print('O texto está vazio')
        return
    
    palavras = filtrar_palavras_longas(entrada)
    if palavras:
        print(f'Palavras longas encontradas: {', '.join(palavras)}')
    else:
        print('Nenhuma palavra longa foi encontrada no texto.')

if __name__ == '__main__':
    main()
