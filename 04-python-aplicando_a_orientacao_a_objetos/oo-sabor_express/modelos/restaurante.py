from modelos.avaliacao import Avaliacao


class Restaurante:
    """Representa um restaurante e suas características"""

    restaurantes = []

    def __init__(self, nome: str, categoria: str) -> None:
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
            - nome (str): O nome do restaurante.
            - categoria (str): A categoria do restaurante.
        """

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        """Retorna uma representação em string do restaurante."""

        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls) -> None:
        """Exibe uma lista formatada de todos os restaurantes."""

        print()
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | Status')
        for restaurante in cls.restaurantes:
            print(
                f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | ⭐ {str(restaurante.media_avaliacoes).ljust(17)} | {restaurante.ativo}')

    @property
    def ativo(self) -> str:
        """Retorna um símbolo indicando o estado de atividade do restaurante."""

        return '✅' if self._ativo else '🔒'

    def alternar_estado(self) -> None:
        """Alterna o estado de atividade do restaurante."""

        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: str, nota: float) -> None:
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
            - cliente (str): O nome do cliente que fez a avaliação.
            - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """

        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self) -> float:
        """Calcula e retorna a média das avaliações do restaurante."""

        if not self._avaliacao:
            return '-'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma / len(self._avaliacao), 1)
