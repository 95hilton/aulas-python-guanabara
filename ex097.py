'''Faça um programa que tenha a função chamada escreva(), que receba um texo qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá Mundo')
Saída:
---------
Olá Mundo
---------'''


def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))


escreva('Hilton')
escreva('Programador Python')
escreva('FIM"')
