with open('01_python_basico/texto.txt') as text:
    r = text.readlines()

    print(r)

with open('01_python_basico/texto2.txt', 'w') as txt:
    txt.write('Olá a todos')

with open('01_python_basico/texto2') as text2:
    for linha in text2:
        print(linha)