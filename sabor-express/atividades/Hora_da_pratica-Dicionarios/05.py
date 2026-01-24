frase = 'Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos. Python é conhecido por sua simplicidade e versatilidade.'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)