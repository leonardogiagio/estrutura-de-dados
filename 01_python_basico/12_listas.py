lista = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
lista2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']

lista3 = lista + lista2

print(lista[0])

lista3.append('Gorila gorila')
lista3.remove('Canis familiaris')

# del(lista)

print(lista3)

print()

for elemento in lista3:
    print(elemento)