# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome da cidade: ').strip()

#Tansforma todo o texto digitado em maiusculo para comparar com o texto do programa
print(cidade[:5].upper() == 'SANTO')