'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com nascimento) em um dicionário se por acaso a CTPS for digerente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da nascimento, com quantos anos a pessoa vai se aposentar'''
from datetime import datetime
ano = datetime.now().year
empregado = {}
empregado['nome'] = str(input('Digite o nome: '))
empregado['nascimento'] = int(input('Digite o ano de nascimento: '))
empregado['idade'] = (ano - empregado['nascimento'])
empregado['ctps'] = int(input('Digite o número da sua carteira de trabalho (digite 0 se não possuir): '))

if empregado['ctps'] == 0:
    print(f'Nome: {empregado["nome"]} '
          f'\nIdade: {empregado["nascimento"]}')
else:
    empregado['contratacao'] = int(input('Digite o ano de contratação: '))
    empregado['salario'] = float(input('Digite o seu salário: R$ '))
    empregado['ano_aposentadoria'] = (empregado['contratacao'] + 35)
    empregado['id_aposentadoria'] = empregado['ano_aposentadoria'] - empregado['nascimento']

    print(f'Nome: {empregado["nome"]}'
          f'\nIdade: {empregado["idade"]}'
          f'\nCTPS: {empregado["ctps"]}'
          f'\nAno de contratação: {empregado["contratacao"]}'
          f'\nSalário: R$ {empregado["salario"]:.2f}'
          f'\nAposentadoria: {empregado["id_aposentadoria"]} anos.')
