def aumentar(valor, percentual):
    """
    ## Função para aumentar um valor à partir de um percentual fornecido
    :param valor: recebe o valor a ser calculado aumento pelo programa
    :param percentual: recebe qual o percentual a ser calculado pelo programa
    :return: retorna o valor com percentual aumentado
    """
    valor = valor + (valor * percentual/100)
    return valor


def diminuir(valor, percentual):
    """
    ## Função para diminuir um valor à partir de um percentual fornecido
    :param valor: recebe o valor a ser calculada a redução pelo programa
    :param percentual: recebe qual o percentual a ser calculado pelo programa
    :return: retorna o valor com percentual aumentado
    """
    valor = valor - (valor * percentual / 100)
    return valor


def dobro(valor):
    """
    ## Função para calcular o dobro de um valor
    :param valor: recebe o valor a ser calculado o dobro
    :return: retorna o valor multiplicado por 2
    """
    valor *= 2
    return valor


def metade(valor):
    """
    ## Função para calcular a metade de um valor
    :param valor: recebe o valor a ser calculada a metade
    :return: retorna o valor dividido por 2
    """
    valor /= 2
    return valor


def moeda(valor):
    """
    ## Função para formatar um valor em formato de moeda.
    :param valor: recebe o valor a ser formatado
    :return: retorna o valor já formatado
    """
    valor = f'R$ {valor:.2f}'.replace('.', ',')
    return valor

