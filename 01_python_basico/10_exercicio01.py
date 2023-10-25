# Ler 5 notas e informar a média

soma = 0

for i in range(1, 6):
    nota = float(input('Digite sua {}ª nota: '.format(i)))
    soma = soma + nota

media = soma / 5

print(media)