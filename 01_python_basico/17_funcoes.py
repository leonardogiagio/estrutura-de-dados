# funcao sem parametro e sem retorno

def mensagem():
    print('texto da função')

mensagem()


# funcao com parametro

def mensagem2(texto):
    print(texto)

mensagem2('olá, parametro')


#funcao com parametro e retorno

def soma(a, b):
    """
    Calcula a soma do parametro a e b
    """
    return a + b

resultado = soma(3, 2)
print(resultado)

help(soma)