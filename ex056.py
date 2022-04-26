'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos'''
idade_velho = 0
nome_velho= ''
soma_idade = 0
cont_mulheres = 0
for i in range(0, 4):
    nome = str(input('Digite o nome da pessoa: ')).upper()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: [M] ou [F]: ')).upper()

    if sexo == 'M' and idade > idade_velho:
        nome_velho = nome
        idade_velho = idade

    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

    soma_idade += idade

print('A média de idade do grupo é: {:.0f} anos'.format(soma_idade / 4))
print('O homem mais velho se chama {} e tem {} anos.' .format(nome_velho, idade_velho))
print('Há {} mulheres com menos de 20 anos.' .format(cont_mulheres))
