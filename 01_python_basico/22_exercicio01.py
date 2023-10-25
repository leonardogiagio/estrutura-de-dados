"""
Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
- ValueError: se o usuário digitar um caracter
- ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
- IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
- KeyboardInterrupt: caso o usuário interrompa a execução
"""



while True:
    try:
        lista = []
        
        lista.append(float(input('Digite o primeiro valor: ')))
        lista.append(float(input('Digite o segundo valor: ')))

        resultado = lista[0] / lista[1]
    except ValueError:
        print('Caracter inválido')
    except ZeroDivisionError:
        print('Não é possível dividir por 0')
        del(lista)
    except IndexError:
        print('Index não encontrado na lista')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução')
        break
    else:
        print(f'O resultado da divisão é: {resultado}')
        break
