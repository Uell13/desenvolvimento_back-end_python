"""
Escreva um programa que receba os nomes dos convidados até que o usuário digite 'sair', e ao final mostre a lista de convidados sem repetições.
"""


def validar_input(msg: str) -> str:
    dado = input(msg).strip().lower()
    if dado == 'sair':
        return dado
    if len(dado) < 3:
        raise ValueError('O nome precisa ter no mínimo 3 caracteres.')
    return dado


def criar_lista_convidados() -> set:
    lista_convidados = set()
    print("--- Sistema de Convidados (digite 'sair' para finalizar) ---")

    while True:

        try:
            dado = validar_input(
                'Digite o nome do convidado para adicionar a lista: ')
            if dado == 'sair':
                break
            if dado in lista_convidados:
                print(
                    f'"{dado.title()}" já foi adicionado(a) a lista de convidados.')
                continue
        except ValueError as e:
            print(f'Ocorreu um erro! Erro: {e}')
            continue
        except Exception as e:
            print(f'Ocorreu um erro inesperado! Erro: {e}')
            continue

        lista_convidados.add(dado)
        print(f'"{dado.title()}" adicionado a lista de convidados.')

    return lista_convidados


convidados = criar_lista_convidados()

if convidados:
    convidados_ordenados = sorted(list(convidados))

    if len(convidados_ordenados) > 1:
        inicio = ", ".join(nome.title() for nome in convidados_ordenados[:-1])
        ultimo = convidados_ordenados[-1].title()
        resultado = f"{inicio} e {ultimo}"
    else:
        resultado = convidados_ordenados[0].title()

    print(f'\nConvidados confirmados ({len(convidados)}): {resultado}')
else:
    print('\nA lista está vazia.')
