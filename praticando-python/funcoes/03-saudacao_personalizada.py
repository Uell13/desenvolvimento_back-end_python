'''
Beatriz está desenvolvendo um sistema de atendimento para um site de serviços.
Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";
Entre 12h e 18h, exibir "Boa tarde";
Após 18h, exibir "Boa noite".
'''

def saudacao_personalizada(hora):
    if 0 <= hora < 12:
        return 'Bom dia!'
    elif 12 <= hora < 18:
        return 'Boa tarde!'
    elif 18 <= hora <= 23:
        return 'Boa noite!'
    else:
        return 'Hora inválida!'

while True:
    try:
        hora = int(input('Informe a hora atual (0-23): '))
        if hora < 0 or hora > 23:
            print('Valor inválido! A hora deve ser um número entre 0 e 23')
            continue
        break
    except:
        print('Valor inválido! O valor deve ser um número inteiro entre 0 e 23')

print(saudacao_personalizada(hora))
