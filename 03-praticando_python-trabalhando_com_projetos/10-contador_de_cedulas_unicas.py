"""
Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor.
O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada
caso não seja digitado um valor numérico válido.
"""


class CaixaEletronico:
    def __init__(self):
        self._cedulas_disponiveis = [100, 50, 20, 10, 5, 2]
        self._cedulas_disponiveis.sort(reverse=True)
        self._resultado = {}

    def realizar_saque(self, valor: int, index: int = 0):
        try:
            valor = int(valor)
        except ValueError:
            raise ValueError('O valor fornecido deve ser um numero inteiro.')
        if valor <= 0:
            raise ValueError('O valor de saque não pode ser negativo ou igual a zero.')
        resultado = self._sacar_dinheiro(valor, index)
        if resultado == None:
            return 'Não foi possível realizar o saque!'
        return dict(sorted(resultado.items(), reverse=True))


    def _sacar_dinheiro(self, valor: float, index=0) -> dict:
        # Caso base: Se o valor for igual a zero, conseguimos o saque
        if valor == 0:
            return {}

        # Se percorreu todas as cédulas e sobrou valor, retorna None e tenta diminuir a quantidade de notas anterior
        if index >= len(self._cedulas_disponiveis):
            return None

        cedula = self._cedulas_disponiveis[index]
        max_notas = int(valor // cedula)

        for quantidade in range(max_notas, -1, -1):
            resto = valor - (quantidade * cedula)
            resultado_subsequente = self._sacar_dinheiro(resto, index + 1)

            if resultado_subsequente is not None:
                if quantidade > 0:
                    resultado_subsequente[cedula] = quantidade
                return resultado_subsequente

        return None


if __name__ == '__main__':
    try:
        c1 = CaixaEletronico()
        resultado = c1.realizar_saque(188)
        if isinstance(resultado, dict):
            print(f"{'=' * 30}")
            print(f"{'DETALHAMENTO DO SAQUE':^30}")
            print(f"{'=' * 30}")
            for cedula, quantidade in resultado.items():
                print(f"• {quantidade} nota(s) de R$ {cedula},00")
            print(f"{'=' * 30}")
        else:
            print(resultado)
    except (ValueError, TypeError) as e:
        print(f'Não foi possível realizar o saque!\nErro: {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado:\n{e}')
