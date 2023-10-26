"""
1 - Crie uma classe chamada aluno com os seguintes atributos:
- Nome
- Nota 1
- Nota 2
- Crie um construtor para a classe (__init__)


2 - Crie as seguintes funções (métodos):
- Calcula média, retornando a média aritmética entre as notas
- Mostra dados, que somente imprime o valor de todos os atributos
- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)

3 - Crie dois objetos (aluno1 e aluno2) e teste as funções
"""

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calculoMedia(self):
        return (self.nota1 + self.nota2) / 2
    
    def mostraDados(self):
        print(self.nome, self.nota1, self.nota2)

    def resultado(self):
        media = self.calculoMedia()
        if(media >= 6):
            return 'Aprovado'
        return 'Reprovado'
    

aluno1 = Aluno('Leonardo', 10, 9)
aluno1.mostraDados()
print(aluno1.calculoMedia())
print(aluno1.resultado())

aluno2 = Aluno('João', 5, 4)
aluno2.mostraDados()
print(aluno2.calculoMedia())
print(aluno2.resultado())