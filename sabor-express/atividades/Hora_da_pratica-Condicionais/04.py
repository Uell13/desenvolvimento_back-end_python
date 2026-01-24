dado_x = float(input('Informe a posição x: '))
dado_y = float(input('Informe a posição y: '))

if dado_x > 0 and dado_y > 0:
    print('Primeiro Quadrante')
elif dado_x < 0 and dado_y > 0:
    print('Segundo Quadrante')
elif dado_x < 0 and dado_y < 0:
    print('Terceiro Quadrante')
elif dado_x > 0 and dado_y < 0:
    print('Quarto Quadrante')
else:
    print('O ponto está localizado no eixo ou origem.')