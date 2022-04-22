"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00 calcule um aumente do 10%.
Para inferiores ou iguais o aumento é de 15%"""

salario = float(input('Digite o salário: '))
aumento = 0

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

salario = salario+aumento
print('Seu aumento será de \033[1;32mR${:.2f}\033[m e seu salário atual ficará em: \033[1;32mR${:.2f}\033[m.' .format(aumento, salario))

