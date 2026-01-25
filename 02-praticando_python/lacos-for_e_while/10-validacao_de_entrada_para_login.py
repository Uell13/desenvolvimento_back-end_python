'''
João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.
'''

import os

nome_usuario = ''
senha = ''

titulo = 'Sistema de Cadastro - Buscante'

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo_cadastro():
    print('-' * len(titulo))
    print(titulo)
    print('-' * len(titulo))

limpar_terminal()
titulo_cadastro()

while True:
    print() # Espaço em branco para melhor visualização
    nome_usuario = input('Digite um nome de usuário (mínimo 5 caracteres): ')

    if len(nome_usuario) < 5:
        input('Nome de usuário inválido. Pressione Enter para tentar novamente...')
        limpar_terminal()
        titulo_cadastro()
        continue

    break

while True:

    limpar_terminal()
    titulo_cadastro()
    print() # Espaço em branco para melhor visualização
    print(f'Nome de usuário: {nome_usuario}')
    print() # Espaço em branco para melhor visualização

    senha = input('Digite uma senha (mínimo 8 caracteres): ')

    if len(senha) < 8:
        input('Senha inválida. Pressione Enter para tentar novamente...')
        limpar_terminal()
        titulo_cadastro()
        continue

    break

limpar_terminal()
titulo_cadastro()
print() # Espaço em branco para melhor visualização
print('Cadastro realizado com sucesso!')
print(f'''
    Dados cadastrados:
    
    Nome do usuário: {nome_usuario}
    senha: {'*' * len(senha)}
''')
