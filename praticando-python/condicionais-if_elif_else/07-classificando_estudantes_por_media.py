nota_01 = float(input('Digite a primeira nota: '))
nota_02 = float(input('Digite a segunda nota: '))
nota_03 = float(input('Digite a terceira nota: '))

media = (nota_01 + nota_02 + nota_03) / 3

if media >= 7:
    print(f'Aluno aprovado com média {media:.2f}')
elif media >= 5:
    print(f'Aluno em recuperação com média {media:.2f}')
else:
    print(f'Aluno reprovado com média {media:.2f}')