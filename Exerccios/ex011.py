print('-' * 10, 'Calculo de M²', '-' * 10)
x = float(input('Digite a largura: '))
y = float(input('Digite a Altura: '))
print('Baseado nas informações obitidas, as segunites dimensões são: {}x{}'.format(x, y,), end=' ')
print('Sua área é de {}m²'.format(x*y))
z = x*y
print('Baseado em sua área a quntidade de tinta necessaria é de {}l'.format(z/2))