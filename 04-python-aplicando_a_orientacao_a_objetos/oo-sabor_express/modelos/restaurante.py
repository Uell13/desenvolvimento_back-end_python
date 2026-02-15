class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str) -> None:
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
        for restaurante in cls.restaurantes:
            print(
                f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante1 = Restaurante('Praça', 'Gourmet')
restaurante2 = Restaurante('Pizza Express', 'Italiana')

restaurante1.alternar_estado()

Restaurante.listar_restaurantes()
