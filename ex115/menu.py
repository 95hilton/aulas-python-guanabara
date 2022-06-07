from colorama import Fore, Style
import cadastro
import visualiza


def menuPrincipal():

    print('='*30)
    print('MENU PRINCIPAL'.center(30))
    print('=' * 30)
    print(Fore.YELLOW, f'1 -{Fore.BLUE} Ver pessoas cadastradas')
    print(Fore.YELLOW, f'2 -{Fore.BLUE} Cadastrar nova pessoa')
    print(Fore.YELLOW, f'3 -{Fore.BLUE} Sair do sistema', Style.RESET_ALL)
    print('=' * 30)
    while True:
        try:
            opcao = int(input(f'{Fore.YELLOW}Sua opção: {Style.RESET_ALL}'))
        except KeyboardInterrupt:
            print('\nO usuário decidiu encerrar o programa.')
            break
        except (ValueError, TypeError):
            print(f'{Fore.RED}Opção inválida, tente novamente.{Style.RESET_ALL}')
        else:
            if opcao == 1:
                visualiza.visualizarPessoas()
                break
            elif opcao == 2:
                cadastro.cadastraPessoa()
                break
            elif opcao == 3:
                print('Saindo do sistema...')
                print('=' * 30)
                break
            else:
                print(f'{Fore.RED}Opção inválida, tente novamente.{Style.RESET_ALL}')
