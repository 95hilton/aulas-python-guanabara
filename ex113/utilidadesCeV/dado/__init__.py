def leiaDinheiro(texto):
    """
    ##Função para validar se texto digitado está em formato numérico para cálculo
    :param texto: string a ser exibida para o usuário solicitando o input
    :return: retorna o valor digitado para o programa
    """
    while True:
        valor = str(input(texto).replace(',', '.')).strip()
        if valor.isalpha():
            print(f'\033[1;41mERRO! {valor} é um preço inválido!\033[m')
        else:
            return float(valor)
            break


def leiaInt(i):
    while True:
        try:
            num = int(input(i))
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO, digite um número inteiro válido!\033[m')
        else:
            return num
            break


def leiaFloat(f):
    while True:
        try:
            num = float(input(f))
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO, digite um número real válido!\033[m')
        else:
            return num
            break
