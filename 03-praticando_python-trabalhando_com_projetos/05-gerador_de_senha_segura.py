# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial.
# Exiba a senha gerada.

import string
import random

def gerar_senha(
    tamanho: int = 8,
    maiuscula: bool = False,
    numero: bool = False,
    especial: bool = False
) -> str:
    '''
    Gera uma senha com caracteres aleatórios com o formato padrão de 8 caracteres de letras minúsculas
    
    :param tamanho: Quantidade de caracteres que deve ser gerado na senha
    :type tamanho: int
    :param maiuscula: A senha deve conter letras maiúsculas?
    :type maiuscula: bool
    :param numero: A senha deve conter números?
    :type numero: bool
    :param especial: A senha deve ter caracteres especiais?
    :type especial: bool
    :return: Retorna uma string informando a senha gerada
    :rtype: str
    '''
    
    # Começa com letras minúsculas como base
    caracteres = string.ascii_lowercase
    senha = [random.choice(string.ascii_lowercase)]
    
    if maiuscula:
        caracteres += string.ascii_uppercase
        senha.append(random.choice(string.ascii_uppercase))
    if numero:
        caracteres += string.digits
        senha.append(random.choice(string.digits))
    if especial:
        caracteres += string.punctuation
        senha.append(random.choice(string.punctuation))
    
    senha.extend(random.choice(caracteres) for _ in range(tamanho - 4))
    random.shuffle(senha)
    
    return ''.join(senha)

def main():
    senha = gerar_senha(tamanho=12,maiuscula=True,numero=True,especial=True)
    print(f'Senha gerada: {senha}')

if __name__ == '__main__':
    main()
