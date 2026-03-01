vendas = {
    'Eletrônicos': [
        {'produto': 'Smartphone', 'quantidade': 5, 'valor_unitario': 2000},
        {'produto': 'Tablet', 'quantidade': 3, 'valor_unitario': 1500}
    ],
    'Eletrodomésticos': [
        {'produto': 'Geladeira', 'quantidade': 2, 'valor_unitario': 3000},
        {'produto': 'Micro-ondas', 'quantidade': 4, 'valor_unitario': 800}
    ],
    'Livros': [
        {'produto': 'Livro A', 'quantidade': 10, 'valor_unitario': 50},
        {'produto': 'Livro B', 'quantidade': 5, 'valor_unitario': 100}
    ]
}

resumo = {}
for categoria in vendas.keys():
    for i in range(len(vendas[categoria])):
        resumo[categoria] = resumo.get(categoria, 0) + (
                vendas[categoria][i]['valor_unitario'] * vendas[categoria][i]['quantidade'])

print(
    f'\nTotal de vendas por categoria:\n{'\n'.join(f'- {categoria}: R$ {valor_total:,.2f}' for categoria, valor_total in resumo.items())}')
