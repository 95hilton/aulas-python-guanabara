'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função.'''


def notas(*n, sit=False):
    """
    ## Função para analisar notas e situação de vários alunos.
    :param n: recebe uma ou mais notas dos alunos
    :param sit: valor opcional, define se o programa irá exibir ou não a situação do aluno
    :return: retorna um dicionario com várias informações sobre o aluno
    """
    r = dict()
    cont = 0
    maior = 0
    menor = 0
    soma = 0

    while cont < len(n):
        if cont == 0:
            menor = n[cont]
        if n[cont] > maior:
            maior = n[cont]
        if n[cont] < menor:
            menor = n[cont]
        print(n[cont])
        soma += n[cont]
        cont += 1

    media = soma / cont
    r['total'] = cont
    r['maior'] = maior
    r['menor'] = menor
    r['media'] = f'{media:.3}'

    if sit:
        if media <= 5:
            r['situacao'] = 'RUIM'
        elif 5 < media <= 7:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'ÓTIMA'
    return r


resp = notas(5.5, 2.5, 6.5, 1.2, sit=True)
print(resp)
help(notas)
