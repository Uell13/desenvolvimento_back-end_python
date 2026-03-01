"""
O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante.
O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.

Exemplo de entrada:
participantes = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
}

Saída esperada:
Lista atualizada de participantes:
Workshop 1: {'Alice', 'Bruno', 'Diego'}
Workshop 2: {'Fernanda', 'Gustavo', 'Helena'}
"""

participantes = {
    'Workshop 1': {'alice', 'bruno', 'carla', 'diego'},
    'Workshop 2': {'fernanda', 'gustavo', 'helena'}
}


def remover_participante(nome: str) -> bool:
    status = False
    for chave in participantes.keys():
        if nome in participantes[chave]:
            participantes[chave].discard(nome)
            status = True
    return status


if __name__ == '__main__':
    print(f'\nParticipantes registrados:')
    print(
        f'{'\n'.join(f'{chave} - {', '.join(f'{p.title()}' for p in lista)}' for chave, lista in participantes.items())}')

    print(f'\nInforme o nome do participante a ser removido:')
    resposta = input('# ').lower().strip()

    if remover_participante(resposta):
        print(f'\n"{resposta.title()}" foi removido(a) da lista de participantes.')
        print(f'\nLista atualizada de participantes:')
        print(
            f'{'\n'.join(f'{chave} - {', '.join(f'{p.title()}' for p in lista)}' for chave, lista in participantes.items())}')
    else:
        print(f'\n"{resposta.title()}" não foi encontrado na lista de participantes.')
