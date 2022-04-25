"""Refaça o DESAFIO 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isosceles: dois lados iguais
- Escaleno: todos os lados diferentes"""

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 == r2 == r3:
    print('Será formado um triangulo EQUILÁTERO!')
elif (r1 == r2) or (r1 == r3) or (r2 == r3):
    print('Será formado um triangulo ISÓSCELES!')
else:
    print('Será formado um triangulo ESCALENO!')
