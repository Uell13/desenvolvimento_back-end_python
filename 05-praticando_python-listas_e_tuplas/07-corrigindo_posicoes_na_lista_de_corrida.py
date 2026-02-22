"""
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes.
Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

Exemplo de Entrada:
Digite o nome incorreto: Carlos
Digite o nome correto: João

Saída esperada:
O nome Carlos foi substituído por João.
Lista atualizada: ['Ana', 'João', 'Pedro']
"""

classificacao = ['Ana', 'Carlos', 'Pedro']
print(f'\nLista de classificacao atual: {classificacao}')

nome_incorreto = input('Digite o nome incorreto: ').strip()
if not nome_incorreto in classificacao:
    print(f'\nO nome "{nome_incorreto}" não está na lista.')
else:
    nome_correto = input('Digite o nome correto: ').strip()
    for i, p in enumerate(classificacao):
        if p == nome_incorreto:
            classificacao[i] = nome_correto
            print(f'\nO nome "{nome_incorreto}" foi substituído por "{nome_correto}".')

print(f'\nLista de classificação:\n{classificacao}')
