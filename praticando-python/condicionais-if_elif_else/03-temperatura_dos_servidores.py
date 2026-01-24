temperatura = float(input('Informe a temperatura atual da sala dos servidores (em °C): '))

if temperatura > 25:
    print('Alerta: A temperatura está acima do recomendado! Verifique o sistema de refrigeração.')
else:
    print('A temperatura está dentro do limite recomendado.')