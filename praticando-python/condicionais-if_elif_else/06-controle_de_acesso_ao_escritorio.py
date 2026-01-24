hora_agora = int(input('Informe a hora atual (0-23): '))

if 8 <= hora_agora < 18:
    print('Acesso permitido. Bem-vindo ao escritório!')
else:
    print('Acesso negado. O escritório está fechado neste horário.')