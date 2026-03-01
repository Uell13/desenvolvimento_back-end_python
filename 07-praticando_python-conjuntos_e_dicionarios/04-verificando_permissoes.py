"""
Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.
"""

permissoes_principais = set(['leitura', 'escrita', 'execução', 'compartilhamento'])
permissoes_solicitadas = set(['leitura', 'exclusão'])

# Retorna True se todos os itens deste conjunto estiverem presentes em outro conjunto maior.
if permissoes_solicitadas < permissoes_principais:
    print('As permissões solicitadas fazem parte das permissões principais.')
else:
    print('As permissões solicitadas não fazem parte das permissões principais.')
