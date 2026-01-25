import time
contador = 0

print() # Espaço em branco para melhor visualização
while contador < 10:
    print('Processando dados...')
    contador += 1 # Atualiza o contador para evitar o loop infinito
    time.sleep(.5)
