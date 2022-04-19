#Escreva um program que leia um valor em metros e o exiba convertido em centímetros e milímetros
metros = float(input('Digite o valor em metros: '))
print('O valor {} metros representa: \n{} em centímetros; \n{} em milímetros' .format(metros, metros*100, metros*1000))