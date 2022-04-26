""""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5: REPROVADO
- Média entre 5 e 6.9: RECUPERAÇÃO
- Média 7 ou superior: APROVADO"""


nota1 = float(input('Digite a nota da PRIMEIRA matéria: '))
nota2 = float(input('Digite a nota da SEGUNDA matéria: '))
media = (nota1 + nota2)/2

if media < 5:
    print('Sua média foi {:.1f}, e você foi REPROVADO' .format(media))
elif 5 <= media < 7:
    print('Sua média foi {:.1f}, e você está de RECUPERAÇÃO' .format(media))
else:
    print('Sua média foi {:.1f}, e você foi APROVADO!' .format(media))
