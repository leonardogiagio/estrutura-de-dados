"""
Dicionário: Crie um dicionário para armazenar o nome e a 
nota de 3 alunos, fazendo a leitura dos valores por meio 
de uma estrutura de repetição. 
Depois, crie uma nova estrutura de repetição para somar 
todas as notas e retornar a média
"""

alunos = {}

for _ in range(1, 4):
    aluno = str(input('Aluno: '))
    nota = float(input('Nota: '))

    alunos[aluno] = nota

soma = 0
media = 0
for aluno, nota in alunos.items():
    soma += nota

media = soma / 3

print(media)