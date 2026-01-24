livros = ['1984', 'Dom Casmurro', 'O Pequeno Príncipe', 'O Hobbit', 'Orgulho e Preconceito']

livro_desejado = 'O Hobbit'
livro_encontrado = False

print() # Espaço em branco para melhor visualização
for livro in livros:
    if livro == livro_desejado:
        livro_encontrado = True
        print(f'Livro encontrado: {livro}')
        break # Sai do loop quando o livro é encontrado

if not livro_encontrado:
    print(f'O livro "{livro_desejado}" não foi encontrado na lista.')
