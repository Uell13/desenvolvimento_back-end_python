"""
Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação.
À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.

Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

Exemplo de Entrada:
Digite o nome do voluntário (ou 'sair' para encerrar): Ana
Digite o nome do voluntário (ou 'sair' para encerrar): João
Digite o nome do voluntário (ou 'sair' para encerrar): Mariana
Digite o nome do voluntário (ou 'sair' para encerrar): sair

Saída esperada:
Voluntários registrados: ['Ana', 'João', 'Mariana']
"""


def validar_dado(nome_voluntario: str):
    if not nome_voluntario or nome_voluntario == '':
        raise ValueError('O campo está vazio, tente de novo.')
    if not nome_voluntario.isalpha():
        raise ValueError('Você deve digitar apenas letras nesse campo!')
    if len(nome_voluntario) < 3:
        raise ValueError(
            'O nome do voluntário deve ter no mínimo 3 caracteres!')


def registrar_voluntarios():
    voluntarios = []
    while True:
        dado = input(
            'Digite o nome do voluntário (ou "sair" para encerrar): ').strip().lower()
        if dado == 'sair':
            break

        try:
            validar_dado(dado)
        except ValueError as e:
            print(f'Erro! {e}')
            continue
        except Exception as e:
            print(f'Erro inesperado! {e}')
            continue

        voluntarios.append(dado)
    imprimir_lista(voluntarios)


def imprimir_lista(lista_voluntarios: list):
    print('\nVoluntários registrados:')
    for voluntario in sorted(lista_voluntarios):
        print(f'• {voluntario.capitalize()}')


registrar_voluntarios()
