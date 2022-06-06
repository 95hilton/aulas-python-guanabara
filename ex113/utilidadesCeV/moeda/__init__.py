def aumentar(valor, percentual, formatar=False):
    """
    ## Função para aumentar um valor à partir de um percentual fornecido
    :param formatar: define se o valor digitado será formatado ou não pela função moeda.
    :param valor: recebe o valor a ser calculado aumento pelo programa
    :param percentual: recebe qual o percentual a ser calculado pelo programa
    :return: retorna o valor com percentual aumentado
    """
    valor = valor + (valor * percentual/100)
    return valor if formatar is False else moeda(valor)


def diminuir(valor, percentual, formatar=False):
    """
    ## Função para diminuir um valor à partir de um percentual fornecido
    :param formatar: define se o valor digitado será formatado ou não pela função moeda.
    :param valor: recebe o valor a ser calculada a redução pelo programa
    :param percentual: recebe qual o percentual a ser calculado pelo programa
    :return: retorna o valor com percentual aumentado
    """
    valor = valor - (valor * percentual / 100)
    return valor if formatar is False else moeda(valor)


def dobro(valor, formatar=False):
    """
    ## Função para calcular o dobro de um valor
    :param formatar: define se o valor digitado será formatado ou não pela função moeda.
    :param valor: recebe o valor a ser calculado o dobro
    :return: retorna o valor multiplicado por 2
    """
    valor *= 2
    return valor if formatar is False else moeda(valor)


def metade(valor, formatar=False):
    """
    ## Função para calcular a metade de um valor
    :param formatar: define se o valor digitado será formatado ou não pela função moeda.
    :param valor: recebe o valor a ser calculada a metade
    :return: retorna o valor dividido por 2
    """
    valor /= 2
    return valor if formatar is False else moeda(valor)


def moeda(valor):
    """
    ## Função para formatar um valor em formato de moeda.
    :param valor: recebe o valor a ser formatado
    :return: retorna o valor já formatado
    """
    valor = f'R$ {valor:.2f}'.replace('.', ',')
    return valor


def resumo(valor, aumento, reducao):
    print('='*40)
    print('RESUMO DO VALOR'.center(40))
    print('=' * 40)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de reducao: \t{diminuir(valor, reducao, True)}')
    print('=' * 40)
