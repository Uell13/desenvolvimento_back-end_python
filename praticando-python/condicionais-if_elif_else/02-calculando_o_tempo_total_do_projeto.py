atividade_a = int(input('Informe o tempo gasto na atividade A (em dias): '))
atividade_b = int(input('Informe o tempo gasto na atividade B (em dias): '))
atividade_c = int(input('Informe o tempo gasto na atividade C (em dias): '))

if atividade_a < 0 or atividade_b < 0 or atividade_c < 0:
    print('Erro: O tempo gasto em cada atividade não pode ser negativo.')
    exit()

tempo_total = atividade_a + atividade_b + atividade_c
print(f'O tempo total do projeto é de "{tempo_total}" dias.')