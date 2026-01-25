usuario = 'josuell'
senha = '12345'

dado_usuario = input('Digite o seu nome de usuário: ')
dado_senha = input('Digite a sua senha: ')

if usuario == dado_usuario and senha == dado_senha:
    print('Login realizado com sucesso!')
else:
    print('O nome de usuário ou senha está inválido!')
    