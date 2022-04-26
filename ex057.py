'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto'''
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo M ou F: ')).upper()
    print(sexo)

print('Obrigado pela resposta. Sexo escolhido: {}.' .format(sexo))
