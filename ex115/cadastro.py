import menu


def cadastraPessoa():
    print('=' * 30)
    print('NOVO CADASTRO'.center(30))
    print('=' * 30)
    try:
        nome = str(input('Nome: '))
    except KeyboardInterrupt:
        print('Digitação interrompida pelo usuário.')
    except:
        print('Não foi possível cadastrar o nome.')
    try:
        idade = int(input('Idade: '))
    except (ValueError, TypeError):
        print('Digitação interrompida pelo usuário.')
    else:
        print(f'Novo registro de {nome} adicionado.')

    try:
        arquivo = open('cadastro.txt', 'a', encoding='utf-8')
    except FileNotFoundError:
        print('Arquivo de texto inexistente. Criando o arquivo.')
        arquivo = open('cadastro.txt', 'w')
    else:
        try:
            arquivo.write(f'\n{nome}\t\t\t{idade} anos')
            arquivo.close()
        except:
            print('Erro ao salvar o arquivo.')

    menu.menuPrincipal()
