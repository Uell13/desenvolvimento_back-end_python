'''
Crie um programa que utilize um laço for para exibir as seguintes mensagens:

Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
'''
import time

print() # Espaço em branco para melhor visualização
for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {segundos} segundos restantes.')
    
    time.sleep(1) # Pausa para melhor visualização da contagem

print() # Espaço em branco para melhor visualização
print('Aproveite a promoção agora!')
