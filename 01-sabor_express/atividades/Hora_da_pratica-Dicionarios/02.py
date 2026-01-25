# 2 - Utilizando o dicionário criado no item 1:
pessoa = {
    'nome': 'Ana',
    'idade': 28,
    'cidade': 'São Paulo'
}

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
pessoa['idade'] = 30

# Adicione um campo de profissão para essa pessoa;
pessoa['profissao'] = 'Padeira'

# Remova um item do dicionário.
del pessoa['cidade']

print(pessoa)