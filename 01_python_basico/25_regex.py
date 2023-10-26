"""
. - qualquer caractere
\w - qualquer caractere alfanumerico
\W - qualquer caractere nao-alfanumerico
\d - qualquer caractere que seja um digito(0-9)
\D - qualquer caractere nao digito
\s - espaço em branco
^ - começa com
$ - termina com
"/" - usado antes de metacaracteres para especificar seu significado literal


QUANTIFICADORES
[] - opcional entre os que estao dentro dos colchetes
() - captura grupo de caracteres
* - de zero a mais vezes
? - zero ou uma vez
+ - uma ou mais vezes
{m, n} - de m a n vezes
| - ou
"""

import re

# inicio search

frase = 'Olá, meu número de telefone é (42)00000-0000'
regex = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)
print(regex)
print()

frase = 'A placa de carro que eu anotei durante o acidente foi FRT-1998'
regex = re.search('[A-Z]{3}-\d{4}', frase)
print(regex)
print()

email = 'Entre em contato, meu email é teste@teste.com'
regex = re.search('\w+@\w+\.\w+', email)
print(regex)
print()

# fim search

# inicio match

frase = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
regex = re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase)
print(regex)
print()

for numero in regex:
    print(numero)
print()

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''
regex = re.findall('\w+@\w+\..+', emails)
print(regex)

# fim match