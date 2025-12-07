#Crie uma classe Pessoa com atributos nome e idade.
# Depois crie uma classe Estudante que herda de Pessoa 
# e adiciona matricula e curso. 
class Pessoa:
    def __init__ (self,nome,idade):
        self.nome= nome
        self.idade= idade
class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        Pessoa.__init__(self, nome,idade)
        self.matricula= matricula
        self.curso= curso
p2= Estudante('Lira',19,112121212, 'Design')
print(f'Aluno(a): {p2.nome}\nidade: {p2.idade} anos\nmatricula: {p2.matricula}\ncurso: {p2.curso}')
