"""
Sua tarefa é criar um programa que solicite o nome do produto e a nova quantidade, atualizando essa informação no dicionário de estoque.
"""

estoque = {
    'caderno universitário': 50,
    'caneta azul': 120,
    'borracha branca': 30
}


def atualizar_estoque(produto: str, quantidade: int) -> bool:
    if produto not in estoque:
        return False
    estoque[produto] = quantidade
    return True


if __name__ == '__main__':
    print(f'\n{estoque}\nDigite dessa forma para atualizar o estoque: "nome do produto = nova quantidade"')
    resposta = [dado.strip() for dado in input('# ').lower().strip().split('=') if dado.strip()]
    if len(resposta) != 2:
        print('\nErro! Use "nome do produto = nova quantidade" para atualizar o estoque.')
        exit()
    try:
        produto, quantidade = resposta
        quantidade = int(quantidade)
    except Exception:
        print('\nErro! A quantidade deve ser um valor inteiro.')
        exit()
    if atualizar_estoque(produto, quantidade):
        print(f'\n{produto} foi atualizado com sucesso!\n{estoque}')
    else:
        print('\nErro! O produto informado não está listado no estoque.')
