'''
A Lógica dos Dígitos Verificadores
O cálculo utiliza algoritmos de módulo 11. Funciona assim:
Primeiro Dígito: Multiplicamos os 9 primeiros dígitos por uma sequência decrescente de 10 a 2. Somamos tudo e aplicamos uma regra de resto de divisão.
Segundo Dígito: Pegamos os 9 primeiros + o primeiro dígito encontrado e multiplicamos por uma sequência de 11 a 2.
'''

def validate_cpf(msg:str):
    '''
    Recebe a numeração do CPF do usuário por meio do prompt
    e verifica se está tudo nos conformes
    '''

    while True:
        # Adiciona a string vazia somente os números digitados no input
        cpf = ''.join(filter(str.isdigit, input(msg)))
        
        # Verifica se o número de caracteres é 11
        if not len(cpf) == 11:
            print('Erro! Cpf inválido. O número do CPF deve conter apenas 11 digitos.')
            continue

        # Bloqueia sequências repetidas Ex: 111.111.111-11
        if cpf == cpf[0] * 11:
            print('Erro! Cpf inválido. Você não pode fornecer um CPF com sequências repetidas.')
            continue

        # Verifica se o dado recebido tem algo que não seja número
        if not cpf.isdigit():
            print('Erro! Cpf inválido. Um CPF válido deve conter apenas números.')
            continue

        # Confere os digitos verificadores
        # Calculo do primeiro digito verificador
        soma = 0
        for i, multiplicador in enumerate(range(10, 1, -1)):
            soma += int(cpf[i]) * multiplicador
        resto = (soma * 10) % 11
        primeiro_digito = 0 if resto == 10 else resto

        if int(cpf[9]) != primeiro_digito:
            print('Erro! Cpf inválido.')
            continue

        # Calculo do segundo digito verificador
        soma = 0
        for i, multiplicador in enumerate(range(11, 1, -1)):
            soma += int(cpf[i]) * multiplicador
        resto = (soma * 10) % 11
        segundo_digito = 0 if resto == 10 else resto

        if int(cpf[10]) != segundo_digito:
            print('Erro! Cpf inválido.')
            continue

        return 'CPF válido.'

def main():
    cpf = validate_cpf('Informe o CPF: ')
    print(cpf)

if __name__ == '__main__':
    main()
