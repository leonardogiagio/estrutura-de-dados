"""
Ler uma temperatura em graus Celsius e apresentá-la 
convertida em graus Fahrenheit. A fórmula de conversão 
é F = (9 * C + 160) / 5, na qual F é a temperatura em 
Fahrenheit e C é a temperatura em graus Celsius
- Função para ler e retorna o valor da temperatura 
(não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a 
temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como 
parâmetro o valor e fazendo a impressão
"""

def tempCparaF1():
    temperatura = float(input('Temperatura em Cº: '))
    temperaturaF = (9 * temperatura + 160) / 5
    return temperaturaF

print(tempCparaF1())


def tempCparaF2(temperatura):
    temperaturaF = (9 * temperatura + 160) / 5
    return temperaturaF

print(tempCparaF2(30))


def tempCparaF3(temperatura):
    temperaturaF = (9 * temperatura + 160) / 5
    print(temperaturaF)

tempCparaF3(30)