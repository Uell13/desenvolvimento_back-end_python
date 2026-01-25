operacoes = {
    '1': 'adição',
    '2': 'subtração',
    '3': 'multiplicação',
    '4': 'divisão',
}
for indice, valor in operacoes.items():
    print(f'{indice} = {valor}')
opcao = int(input('Escolha a operação: '))

primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

match opcao:
    case 1:
        resultado = (lambda x, y : x + y)(primeiro_numero, segundo_numero)
        print(resultado)
    case 2:
        resultado = (lambda x, y : x - y)(primeiro_numero, segundo_numero)
        print(resultado)
    case 3:
        resultado = (lambda x, y : x * y)(primeiro_numero, segundo_numero)
        print(resultado)
    case 4:
        try:
            resultado = (lambda x, y : x / y)(primeiro_numero, segundo_numero)
            print(resultado)
        except ZeroDivisionError:
            print('Erro! Um número não pode ser dividido por zero.')
    case _:
        print('Operação inválida!')
