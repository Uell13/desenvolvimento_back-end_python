# Crie um programa que ajude Ana a exibir somente os livros que possuem estoque disponível, no formato: "Livro disponível: ".

livros = [
    {'nome': '1984', 'estoque': 5},
    {'nome': 'Dom Casmurro', 'estoque': 0},
    {'nome': 'O Pequeno Príncipe', 'estoque': 3},
    {'nome': 'O Hobbit', 'estoque': 0},
    {'nome': 'Orgulho e Preconceito', 'estoque': 2}
]

print() # Espaço em branco para melhor visualização
for livro in livros:
    if livro['estoque'] == 0:
        continue # Pula para a próxima iteração do loop se o estoque for 0
    print(f'Livro disponível: {livro['nome']}')
