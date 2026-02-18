class Avaliacao:
    """Representa as características de avaliações dadas a um restaurante."""
    
    def __init__(self, cliente: str, nota: float) -> None:
        self._cliente = cliente
        self._nota = nota
