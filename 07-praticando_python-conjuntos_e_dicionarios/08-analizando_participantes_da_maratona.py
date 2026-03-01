"""
Lucas é voluntário na organização de uma maratona e recebeu a lista de participantes com suas respectivas idades.
Agora, ele precisa de um programa que apresente três informações:

Os nomes de todos os participantes.
As idades de todos os participantes.
Uma relação completa com o nome e a idade de cada um.

Sua tarefa é criar esse programa com base nas informações fornecidas.

Exemplo de entrada:
participantes = {
    "Mariana": 25,
    "Carlos": 32,
    "Beatriz": 28,
    "Rafael": 35
}

Saída esperada:
Nomes dos participantes: Mariana, Carlos, Beatriz, Rafael
Idades dos participantes: 25, 32, 28, 35
Participantes e suas idades:
- Mariana: 25 anos
- Carlos: 32 anos
- Beatriz: 28 anos
- Rafael: 35 anos
"""

participantes = {
    'mariana': 25,
    'carlos': 32,
    'beatriz': 28,
    'rafael': 35
}

print(f'\nNomes dos participantes: {', '.join(p.title() for p in participantes.keys())}')
print(f'Idades dos participantes: {', '.join(str(i) for i in participantes.values())}')
print(f'Participantes e suas idades:\n{'\n'.join(f'- {p.title()}: {i} anos' for p, i in participantes.items())}')
