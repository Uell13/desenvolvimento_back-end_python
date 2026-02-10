import random


class JogoNumeroSecreto:
    """
    Representa um jogo de adivinhação de números

    A classe gerencia a lógica de um jogo onde o usuário tenta adivinhar
    um número secreto gerado aleatoriamente dentro de um intervalo definido,
    com um limite de tentativas.

    Atributos:
        numero_maximo (int): O limite superior para o número secreto (padrão 100)
        tentativas_restantes (int): Quantidade de chances que o jogodor possui
    """

    def __init__(self, numero_maximo: int = 100, tentativas: int = 5) -> None:
        self.numero_maximo = numero_maximo
        self.tentativas_restantes = tentativas

    def _gerar_numero_secreto(self) -> int:
        return random.randint(1, self.numero_maximo)

    def _obter_palpite(self, entrada: str) -> int:
        try:
            palpite = int(entrada)
        except ValueError:
            raise ValueError('Entrada inválida: Você deve enviar apenas número inteiro.')
        if palpite < 1 or palpite > self.numero_maximo:
            raise ValueError(
                f'Entrada inválida: Número fora do intervalo! Digite um número entre 1 e {self.numero_maximo}.')
        return palpite

    def rodar_jogo(self):
        numero_secreto = self._gerar_numero_secreto()
        print(f'--- NÚMERO SECRETO (1-{self.numero_maximo}) ---')

        while self.tentativas_restantes > 0:
            print(f'Tentativas: {self.tentativas_restantes}')
            resposta = input(f'Tente adivinhar o número secreto (1-{self.numero_maximo}): ')

            try:
                palpite = self._obter_palpite(resposta)
            except ValueError as e:
                print(e)
                continue

            if palpite == numero_secreto:
                print(f'Parabéns! Você acertou o número secreto.')
                break

            self.tentativas_restantes -= 1
            dica = 'Muito baixo!' if palpite < numero_secreto else 'Muito alto!'
            if self.tentativas_restantes > 0:
                print(f'{dica} Tente novamente.')
            else:
                print(f'Que pena! Suas tentativas acabaram. O número era {numero_secreto}.')

        print(f'FIM DO JOGO!')


if __name__ == '__main__':
    j1 = JogoNumeroSecreto(100, 10)
    j1.rodar_jogo()
