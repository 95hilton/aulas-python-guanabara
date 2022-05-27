'''Faça um programa que tenha uma função chamada área(), que receba as dimensóes de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def area(larg, comp):
    print(f'A área do terreno de {larg}x{comp} é: {larg * comp} m².')


area(float(input('Digite a largura do terreno (m): ')), float(input('Digite o comprimento do terreno (m): ')))
