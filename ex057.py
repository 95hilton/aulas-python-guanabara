'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto'''
sexo = ''
idade = 0

sexo = str(input('Digite o sexo M ou F: ')).upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor informe novamente o sexo: ')).upper()

idade = int(input('Digite a idade: '))
print('Obrigado pela resposta. \nSexo: {}, Idade: {}.' .format(sexo, idade))
