def somar_inteiros(n:int):
    if n == 1:
        return 1
    return n + somar_inteiros(n - 1)

numero = int(input('Digite um número: '))
resultado = somar_inteiros(numero)
print(f'A soma de 1 a {numero} é: {resultado}')
