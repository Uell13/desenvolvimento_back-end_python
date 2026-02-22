from carro import Carro
from moto import Moto

c1 = Carro('Fiat', 'Strada', 2)
c2 = Carro('Volkswagen', 'Polo', 4)
c3 = Carro('Toyota', 'Corolla', 4)

m1 = Moto('Honda', 'CG 160 Titan', 'Casual (Street)')
m2 = Moto('Yamaha', 'Fazer FZ25', 'Casual (Naked)')
m3 = Moto('BMW', 'R 1300 GS', 'Esportiva (Big Trail/Adventure)')

lista_carros = [c1, c2, c3]
lista_motos = [m1, m2, m3]

lista_veiculos = lista_carros + lista_motos

for veiculo in lista_veiculos:
    print(veiculo)
