"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: sobrepeso
- 30 ate 40: obesidade
- Acima de 40: obesidade morbida"""

peso = float(input('Digite o peso da pessoa em KG: '))
altura = float(input('Digite a altura da pessoa em METROS (Ex: 1.82): '))
imc = peso / altura**2


if imc < 18.5:
    print('Seu IMC é: {:.2f} e você está ABAIXO DO PESO.' .format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC é: {:.2f} e você está NO PESO IDEAL.' .format(imc))
elif 25 < imc <= 30:
    print('Seu IMC é: {:.2f} e você tem SOBREPESO.' .format(imc))
elif 30 < imc <= 40:
    print('Seu IMC é: {:.2f} e você está OBESO.' .format(imc))
else:
    print('Seu IMC é: {:.2f} e você tem OBESIDADE MÓRBIDA.'.format(imc))