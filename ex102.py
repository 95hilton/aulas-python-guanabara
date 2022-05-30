'''Crie um program que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(numero, show=False):
    """
    -- Calcula o fatorial de um número.
    :param numero: número a ser calculado
    :param show: opcional - Mostrar ou não a conta
    :return: o valor do fatorial de um número n
    """
    fat = 1
    if show:
        while numero > 1:
            print(f'{numero}', end=' x ')
            fat *= numero
            numero -= 1
        print('1 = ', end=' ')
    else:
        while numero > 1:
            fat *= numero
            numero -= 1
    return fat


print(fatorial(5, True))
help(fatorial)
