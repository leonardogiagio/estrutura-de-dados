"""
Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
- Números
- CEPs
- URLs
"""

import re

frase = '''Proprietário do apartamento: (11) 9999-9999
Amiga de Mariana: (12) 3333-3333
Decorador: (13) 4444-4444'''
regex = re.findall('\(\d{2}\).+\d{4,5}-\d{4}', frase)
print(regex)
print()

frase = 'Meu amigo mora no CEP 22222-000, na cidade do Rio de Janeiro, estado do Rio de Janeiro.'
regex = re.findall('\d{5}-\d{3}', frase)
print(regex)
print()

frase = 'Acesse o site da Wikipedia em https://pt.wikipedia.org/wiki/Wikipedia para aprender mais sobre o mundo.'
regex = re.findall('https?://[A-Za-z0-9./]+', frase)
print(regex)