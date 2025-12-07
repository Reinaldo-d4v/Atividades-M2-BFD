"Modele um sistema escolar simples: "
"● Classe Pessoa (nome, idade) "
"● Classe Aluno (herda de Pessoa, com matrícula e notas)" 
"● Classe Professor (herda de Pessoa, com disciplina e salário)" 
"● Crie métodos para cadastrar notas do aluno e calcular a média." 
"● Crie objetos de alunos e professores e exiba os dados formatados. "

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = []

    def adic_nota(self, nota):
        self.notas.append(nota)

    def media(self):
        return sum(self.notas) / len(self.notas)

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario

alun = Aluno("Lira", 16, "13123B")
alun.adic_nota(3)
alun.adic_nota(9)

prof = Professor("Joaquim", 46, "Quimica", 4454)

print(f"Aluno: {alun.nome}, Idade: {alun.idade}, Matrícula: {alun.matricula}, Média: {alun.media():.2f}")
print(f"Professor: {prof.nome}, Idade: {prof.idade}, Disciplina: {prof.disciplina}, Salário: R${prof.salario}")
