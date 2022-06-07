import menu


def visualizarPessoas():
    print('=' * 30)
    print('PESSOAS CADASTRADAS'.center(30))
    print('=' * 30)
    try:
        with open('cadastro.txt') as arquivo:
            pessoas = arquivo.readlines()
        for p in pessoas:
            print(p)
        arquivo.close()
    except FileNotFoundError:
        print('Não existem pessoas cadastradas!')
    menu.menuPrincipal()
