"""
Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
- Cada aluno deve ocupar uma linha do novo arquivo de texto
- O formato deve ser: nome,nota (Pedro,8.0)
- Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
"""

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('01_python_basico/alunos.txt', 'w') as txt:
    for aluno, nota in alunos.items():
        txt.write(f'{aluno},{nota}\n')

with open('01_python_basico/alunos.txt', 'r') as txt:
    r = txt.readlines()
    print(r)