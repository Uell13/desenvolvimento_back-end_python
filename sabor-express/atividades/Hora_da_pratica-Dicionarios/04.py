# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
meu_dicionario = {
    'nome': 'Carlos',
    'idade': 35,
    'cidade': 'Rio de Janeiro'
}

chave_a_verificar = 'cidade'
if chave_a_verificar in meu_dicionario:
    print(f'A chave "{chave_a_verificar}" existe no dicionário.')
else:
    print(f'A chave "{chave_a_verificar}" não existe no dicionário.')