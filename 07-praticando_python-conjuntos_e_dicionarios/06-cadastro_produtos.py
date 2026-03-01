"""
O sistema deve solicitar o nome e a quantidade de três produtos e, ao final,
exibir as informações cadastradas em um dicionário, onde cada produto será uma chave e a quantidade correspondente será o valor.
"""

produtos = {}

print('\n--- SISTEMA DE CADASTRO DE PRODUTOS ---')
while True:
    print('\nDigite "sair" para finalizar o programa')
    print('Para cadastrar um produtos digite: "nome do produto = quantidade"')
    resposta = input('# ').lower().strip()
    if resposta == 'sair':
        break
    dados = [d.strip() for d in resposta.split('=') if d.strip()]
    if len(dados) != 2:
        print('\nErro! Para cadastrar um produtos digite: "nome do produto = quantidade"')
        continue
    try:
        quantidade = int(dados[1])
    except Exception:
        print('\nErro! A quantidade deve ser um número inteiro.')
        continue

    produtos[dados[0]] = quantidade
    print(
        f'\nProduto cadastrado com sucesso.\nNome do produto: "{dados[0]}"\nQuantidade: {quantidade}')


if len(produtos) == 0 or produtos == {}:
    print('\nNão há produtos cadastrados.')
else:
    print(
        f'\nProdutos cadastrados no sistema:\n{'\n'.join(f'{n.title()} - {q}' for n, q in produtos.items())}')
