class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f'{self.marca} {self.modelo} - Status: {self.ligado}'

    @property
    def ligado(self):
        return 'ligado' if self._ligado else 'desligado'


if __name__ == '__main__':
    v1 = Veiculo('Chevrolet', 'LTZ')
    print(v1)
