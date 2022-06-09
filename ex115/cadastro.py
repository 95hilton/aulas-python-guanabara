import menu


def cadastraPessoa():
    print('=' * 30)
    print('NOVO CADASTRO'.center(30))
    print('=' * 30)
    while True:
        try:
            nome = str(input('Nome: ')).upper().strip()
            if nome != '':
                break
            else:
                print('Digite um nome válido!')
        except KeyboardInterrupt:
            print('Digitação interrompida pelo usuário.')
    while True:
        try:
            idade = int(input('Idade: '))
            if idade != '':
                break
        except KeyboardInterrupt:
            print('Digitação interrompida pelo usuário.')
        except (ValueError, TypeError):
            print('Digite uma idade válida.')

    try:
        arquivo = open('cadastro.txt', 'a', encoding='utf-8')
    except Exception as erro:
        print(f'Erro ao preencher o arquivo: {erro.__class__}.')
    else:
        try:
            arquivo.write(f'{nome}\t\t\t{idade} anos\n')
            arquivo.close()
        except Exception as erro:
            print(f'Erro ao salvar o arquivo: {erro.__class__}')
        else:
            print(f'Novo registro de {nome} adicionado.')

    menu.menuPrincipal()
