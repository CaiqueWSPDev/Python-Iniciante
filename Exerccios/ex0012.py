print('Tira de porcentagem')
print('-'*20)
x = float(input('Digite o valor do produto: R$'))
y = float(input('Digite o valor em % a ser descontado: '))
z = x * y
a = z/100
print('O desconto é de R${:.2f} o valor do produto agora é de: R${:.2f}'.format(a, x-a))
print('-'*20)