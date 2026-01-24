import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizzaria', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiana', 'ativo': False}
]

def limpar_terminal():
    '''
    Essa função é responsável por limpar o terminal.

    Outputs:
    - Limpa o terminal do sistema operacional.
    '''
    os.system('clear')

def exibir_nome_do_programa():
    '''
    Essa função é responsável por exibir o nome do programa.

    Outputs:
    - Exibe no terminal o nome do programa em arte ASCII.
    '''
    print('''
    ╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
    ┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
    ┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
    ╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
    ┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
    ╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
    ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯
    ''')

def exibir_opcoes():
    '''
    Essa função é responsável por exibir as opções do menu principal.

    Outputs:
    - Exibe no terminal as opções disponíveis para o usuário.
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''
    Essa função é responsável por finalizar o programa.

    Outputs:
    - Exibe no terminal uma mensagem de encerramento do programa.
    '''
    exibir_subtitulo('Encerrando o programa...')

def retornar_ao_menu_principal():
    '''
    Essa função é responsável por retornar ao menu principal.

    Outputs:
    - Aguarda o usuário pressionar "enter" para retornar ao menu principal.
    '''
    input('Pressione "enter" para retornar ao menu.. ')
    main()

def opcao_invalida():
    '''
    Essa função é responsável por tratar opções inválidas.

    Outputs:
    - Exibe no terminal uma mensagem informando que a opção escolhida é inválida.
    '''
    print('\nOpção inválida')
    retornar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''
    Essa função é responsável por exibir subtítulos.

    Arguments:
    - texto (str): Texto do subtítulo a ser exibido.

    Outputs:
    - Exibe no terminal o texto fornecido com linhas acima e abaixo.
    '''
    limpar_terminal()
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''
    Essa função é responsável por cadastar um novo restaurante.

    Inputs:
    - nome_do_restaurante: Nome do restaurante a ser cadastrado.
    - categoria_do_restaurante: Categoria do restaurante a ser cadastrado.

    Outputs:
    - Adiciona um novo dicionário na lista de restaurantes com as informações fornecidas.
    '''
    exibir_subtitulo('Cadastro de novo restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_novo_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria_do_restaurante,
        'ativo': False
    }
    restaurantes.append(dados_do_novo_restaurante)

    print(f'O restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!\n')
    retornar_ao_menu_principal()

def listar_restaurantes():
    '''
    Essa função é responsável por listar os restaurantes cadastrados.

    Outputs:
    - Exibe no terminal a lista de restaurantes com seus respectivos nomes, categorias e status (ativo/inativo).
    '''
    exibir_subtitulo('Restaurantes cadastrados')

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_ativo = '(Ativo)' if restaurante['ativo'] else '(Inativo)'
        print(f'{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {status_ativo}')

    print()
    retornar_ao_menu_principal()

def alternar_status_restaurante():
    '''
    Essa função é responsável por alternar o status de um restaurante.

    Inputs:
    - nome_do_restaurante: Nome do restaurante cujo status será alterado.

    Outputs:
    - Altera o status do restaurante para ativo se estiver inativo, ou para inativo se estiver ativo.
    - Exibe uma mensagem no terminal informando o novo status do restaurante.
    '''
    exibir_subtitulo('Alternar status do restaurante')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_do_restaurante.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O status do restaurante "{restaurante['nome']}" foi alterado para (Ativo)' if restaurante['ativo'] else f'O status do restaurante "{restaurante['nome']}" foi alterado para (Inativo)'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante "{nome_do_restaurante}" não foi encontrado.')
    
    print()
    retornar_ao_menu_principal()

def escolher_opcao():
    '''
    Essa função é responsável por escolher a opção no menu principal.

    Inputs:
    - opcao_escolhida: Opção escolhida pelo usuário.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_status_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
    Função principal do programa.
    '''

    limpar_terminal()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
