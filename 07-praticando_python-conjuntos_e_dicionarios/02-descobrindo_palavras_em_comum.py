"""
Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.
"""

texto1 = set('O sol brilha forte no céu azul'.lower().split())
texto2 = set('O céu azul anuncia um dia de sol intenso'.lower().split())

palavras_comum = texto1 & texto2

print(palavras_comum)
