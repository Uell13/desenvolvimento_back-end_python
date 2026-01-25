idade = int(input('Digite a sua idade: '))

if idade > 0 and idade <= 12:
    print('Você é uma criança!')
elif idade >= 13 and idade <= 18:
    print('Você é adolecente!')
elif idade > 18:
    print('Você é adulto!')
else:
    print('Número inválido!')