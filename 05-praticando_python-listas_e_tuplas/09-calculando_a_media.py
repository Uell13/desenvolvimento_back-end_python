"""
A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma.
Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.

Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

Exemplo de Entrada:
Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8

Saída esperada:
Média final da turma: 7.88
"""


def eh_decimal(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def validar_input(msg: str) -> list:
    return [float(n.strip()) for n in input(msg).split(',') if eh_decimal(n) and 0 < float(n) <= 10]

print(
    '\nDigite as notas dos alunos separadas por vírgula'
    '\nExemplo: 8.5, 7.0, 9.2, 6.8'
)
notas = validar_input('$ ')

if not notas or notas == []:
    print('\nA lista de notas está vazia.')
else:
    media = sum(notas) / len(notas)
    print(f'Média final da turma: {media:.2f}')
