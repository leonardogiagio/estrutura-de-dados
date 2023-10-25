a = 'casaco'
print(a)

maiuscula = a.upper()
print(maiuscula)

minuscula = maiuscula.lower()
print(minuscula)

capital = a.capitalize()
print(capital)

metade_palavra = a[0:3]
print(metade_palavra)

ultimas_letras = a[3:]
print(ultimas_letras)

b = a.replace('aco', 'inha')
print(b)

c = a.replace('o', 'a')
print(c)

print(c.find('s'))

e = ' casaco '
print(len(e))

f = e.strip()
print(len(f))

n1 = 14
n2 = 16
print('Dividindo {} por {} o resultado é {}'.format(n1, n2, n1/n2))