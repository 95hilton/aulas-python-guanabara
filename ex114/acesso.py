from urllib import request
from colorama import Fore


def acessaPagina(url):
    """
    ## Função para testar se URL está acessível
    :param url: url da página a ser acessada
    :return: retorna print com status do teste
    """
    try:
        request.urlopen(url)
    except Exception as erro:
        print(Fore.RED, f'Erro ao acessar a página!')
        print(Fore.RED, f'Erro encontrado: {erro.__class__}')
    else:
        print(Fore.GREEN, 'A página está acessível!')
