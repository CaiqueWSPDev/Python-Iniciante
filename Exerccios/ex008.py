n = float(input('Uma distancia em metros: '))
x = n/1000
y = n/100
z = n/10
a = n*10
b = n*100
c = n*1000
print('{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(x, y, z, a, b, c))

#Tbm funciona assim EX.:
# metros = float(input('Digite a distancia: '))
#print('{}cm, {}mm'.format(metros*100, metros*1000))