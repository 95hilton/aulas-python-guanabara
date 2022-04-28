'''Melhore o DESAFIO 061 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

primeiro = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quer mostrar mais quantos termos? '))

print('Progressão finalizada com {} termos exibidos. '.format(total))
