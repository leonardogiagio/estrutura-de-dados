"""
Lista: Crie uma estrutura de repetição para fazer a 
leitura de 5 números inteiros e os armazene dentro de 
uma lista. Após a leitura, crie outra estrutura de 
repetição para somar todos os valores digitados
"""

lista = []

for _ in range(1, 6):
    numero = int(input('Digite um número: '))
    lista.append(numero)

soma = 0
for i in lista:
    soma += i

print(soma)


