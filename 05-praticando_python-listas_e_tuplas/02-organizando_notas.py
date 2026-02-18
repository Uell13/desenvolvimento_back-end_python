"""
Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação.
Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes
e exiba, ao final, essa lista ordenada em ordem crescente.

Exemplo de Entrada:
Notas: [85, 70, 90, 60, 75]

Saída esperada:
Notas ordenadas: [60, 70, 75, 85, 90]
"""

def ordenar_notas(lista: list) -> list:
    lista_tratada = [x for x in lista if isinstance(x, int) or isinstance(x, float)]
    if not lista_tratada:
        raise ValueError('Certifique-se de fornecer somente valores do tipo INT ou FLOAT na lista.')
    return sorted(lista_tratada)

try:
    notas = [85, 70, 90, 60, 75]
    print(ordenar_notas(notas))
except ValueError as e:
    print(f'Erro! {e}')
except Exception as e:
    print(f'Erro inesperado! {e}')
