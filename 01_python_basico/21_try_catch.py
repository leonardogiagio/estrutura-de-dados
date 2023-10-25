"""
while True:

    try:
        number = int(input('Digite um número inteiro: '))
    except:
        print('Valor inválido')
    else:
        print(f'Valor digitado é {number}')
        break
"""

while True:
    try:
        p = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Valor Inválido')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'Valor digitado é {p}')
        break