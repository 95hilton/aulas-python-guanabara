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
