limite_orcamento = 3000
despesas_total = float(input('Informe o total de despesas mensais: R$ '))

if despesas_total > limite_orcamento:
    print('Atenção! Você ultrapassou o limite do seu orçamento mensal.')
else:
    print('Parabéns! Você está dentro do seu orçamento mensal.')