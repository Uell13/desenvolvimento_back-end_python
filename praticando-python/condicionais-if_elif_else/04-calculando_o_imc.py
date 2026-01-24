import os

while True:

    os.system('cls' if os.name == 'nt' else 'clear')
    mensagem = 'Calculadora de IMC (Índice de Massa Corporal)'
    print('-' * len(mensagem))
    print(mensagem)
    print('-' * len(mensagem))
    print()

    try:
        peso = float(input('Informe o seu peso (em Kg): '))
        altura = float(input('Informe a sua altura (em metros): '))

        if peso <= 0 or altura <= 0:
            print('\nErro: Peso e altura devem ser valores positivos. Tente novamente.')
            input('Pressione Enter para tentar novamente... ')
            continue # Volta ao início do loop para solicitar os valores novamente

        break # Sai do loop se os valores forem válidos

    except ValueError:
        print('\nErro: Por favor, insira valores numéricos válidos para peso e altura.')
        input('Pressione Enter para tentar novamente... ')

calculo_imc = peso / (altura ** 2)

print(f'\nSeu IMC é de: "{calculo_imc:.2f}"')

if calculo_imc < 18.5:
    print('Classificação: Abaixo do peso.')
elif calculo_imc < 25:
    print('Classificação: Peso normal.')
elif calculo_imc < 30:
    print('Classificação: Sobrepeso.')
elif calculo_imc < 35:
    print('Classificação: Obesidade grau I.')
elif calculo_imc < 40:
    print('Classificação: Obesidade grau II.')
else:
    print('Classificação: Obesidade grau III ou mórbida.')