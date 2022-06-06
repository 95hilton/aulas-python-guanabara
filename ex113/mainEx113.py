"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função com o nome leiaFloat() com a mesma funcionalidade."""
from utilidadesCeV import dado

i = dado.leiaInt('Digite um número inteiro: ')
r = dado.leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o número real foi {r}!')
