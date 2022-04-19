# Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o salário do funcionário: R$ '))
novo_salario = salario+(salario*0.15)
print('O novo salário do funcionário é: R$ {}' .format(novo_salario))