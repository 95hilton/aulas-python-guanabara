"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal"""

num = int(input('Digite um número inteiro: '))
result = 0
base = int(input("""Digite a base de conversão:
                    \n1 - para binário
                    \n2 - para octal
                    \n3 - para hexadecimal
                    \n """))
if base == 1:
    print('convertendo {} para base BINÁRIO.....\n' .format(num))
    result = bin(num)[2:]
    print('O resultado é: {} '.format(result))
elif base == 2:
    print('convertendo {} para base OCTAL.....\n' .format(num))
    result = oct(num)[2:]
    print('O resultado é: {} '.format(result))
elif base == 3:
    print('convertendo {} para base HEXADECIMAL.....\n'.format(num))
    result = hex(num)[2:]
    print('O resultado é: {} '.format(result))
else:
    print('Opção inválida! Tente novamente mais tarde!')
