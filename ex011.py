# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²
largura = float(input('Digite a largura (em metros) da parede: '))
altura = float(input('Digite a altura (em metros) da parede: '))
area = largura*altura
qtd_tinta = float(area/2)
print('Voce precisara de {} litros de tinta para pintar a parede!' .format(qtd_tinta))
