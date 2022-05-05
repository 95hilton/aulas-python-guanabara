'''Crie um program que leia nome duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
aluno = []
classe = []

while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))

    classe.append(aluno[:])
    aluno.clear()

    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N] ')).strip().upper()

    if continua == 'N':
        print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>8}')
        for n, l in enumerate(classe):
            print(f'{n:<5}{l[0]:<10}{(l[1]+l[2])/2:>8} ')

        individual = 0
        while individual != 999:
            individual = int(input('Deseja exibir notas de qual aluno? (999 interrompe): '))
            if individual == 999:
                break

            if individual <= len(classe) - 1:
                print(f'Exibindo notas do aluno {classe[individual][0]}:\nMatéria A: {classe[individual][1]}\nMatéria B: {classe[individual][1]}')
        break
