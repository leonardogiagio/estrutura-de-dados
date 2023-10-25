import math

a = 5
b = 3

print('A soma é', a + b)
print('A subtração é', a - b)
print('A multiplicação é', a * b)
print('A divisão é', a / b)
print('{} elevado a {} é {}'.format(a, b, a**b))
print('A raíz quadrada de {} é {}'.format(a, math.sqrt(a)))

casos_doenca = 134
numero_habitantes = 34432
casos_por_habitante = casos_doenca / numero_habitantes
print(casos_por_habitante)

casos_por_habitante = round(casos_por_habitante, 6)
print(casos_por_habitante)