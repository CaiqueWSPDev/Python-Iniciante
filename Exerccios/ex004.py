print('Indentificador')
nome = str(input('Digite algo: '))
print('O tipo primitivo desse nome é: {} !'.format(type(nome)))
print('Só tem espços?: {}!\nÉ um numero?: {}\nÉ alfabetico?: {}\nÉ alfanumerico?: {}\nEsta maiuscula?: {}\nEsta minuscula?: {}\nEsta capitalizada?: {}'.format(nome.isspace(),nome.isnumeric(), nome.isalpha(), nome.isalnum(), nome.isupper(), nome.islower(), nome.istitle()))