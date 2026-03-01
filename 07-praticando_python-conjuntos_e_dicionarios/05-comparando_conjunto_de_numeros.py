"""
Após unir as listas, ela quer remover uma tarefa específica informada pelo usuário.
Sua tarefa é criar um programa que realize essa operação.

Exemplo de entrada:
equipe_a = {"planejar reunião", "revisar documento", "testar sistema"} 
equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

Saída esperada:
Tarefas finais: {'implementar funcionalidade', 'planejar reunião', 'revisar documento', 'corrigir bug'}
"""

equipe_a = {'planejar reunião', 'revisar documento', 'testar sistema'}
equipe_b = {'testar sistema', 'implementar funcionalidade', 'corrigir bug'}

# Retorna um conjunto contendo a união dos conjuntos
listas_unidas = equipe_a | equipe_b

while True:
    print(f'\nLista de tarefas: {', '.join(listas_unidas)}\nDeseja remover alguma tarefa específica da lista? (digite: "cancelar" para manter a lista)')
    resposta = input('# ').lower().strip()
    if resposta == 'cancelar':
        break
    if resposta not in listas_unidas:
        print('\nA tarefa informada não foi encontrada na lista! Verifique se digitou corretamente.')
        continue
    listas_unidas.discard(resposta)
    print(f'\nA tarefa "{resposta}" foi removida com sucesso.')
    
print(f'\nLista de tarefas:\n{'\n'.join(listas_unidas)}')
