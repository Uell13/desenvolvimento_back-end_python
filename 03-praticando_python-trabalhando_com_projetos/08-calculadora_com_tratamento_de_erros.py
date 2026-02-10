class Calculadora:
    operadores_validos = {
        '+': lambda num1, num2: num1 + num2,
        '-': lambda num1, num2: num1 - num2,
        '*': lambda num1, num2: num1 * num2,
        '/': lambda num1, num2: num1 / num2
    }

    def __init__(self, num1: float, num2: float) -> None:
        self.num1 = num1
        self.num2 = num2

    def _tratar_erros(self, operador: str) -> list:
        try:
            num1 = float(self.num1)
            num2 = float(self.num2)
        except ValueError:
            raise ValueError('Entrada inválida: Os valores fornecidos não são números válidos.')
        if operador not in self.__class__.operadores_validos:
            raise ValueError(f'O operador "{operador}" é inválido!')
        if operador == '/' and num2 == 0:
            raise ValueError('Erro: Divisão por zero não é permitida!')
        return num1, num2

    def calcular(self, operador: str):
        try:
            num1, num2 = self._tratar_erros(operador)
            resultado = self.__class__.operadores_validos[operador](num1, num2)
            print(f'Resultado: {resultado}')
        except (ValueError, ZeroDivisionError) as e:
            print(f'Não foi possível calcular: {e}')
        except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')


num1 = input('Digite o primeiro número: ')
operacao = input('Escolha a operação (+, -, *, /): ')
num2 = input('Digite o segundo número: ')
c1 = Calculadora(num1, num2)
c1.calcular(operacao)
