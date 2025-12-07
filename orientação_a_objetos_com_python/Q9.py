# Crie uma classe Professor que herda de Funcionario 
# e adiciona a propriedade disciplina.
# Crie um método que exiba "Professor X leciona Y". 
 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario, meses_d_servico):
        super().__init__(nome, idade)
        self.salario = salario
        self.meses_d_servico = meses_d_servico
        self.decimo_terceiro = None
    
    def calc_decimo_3(self):
        self.decimo_terceiro = self.salario * self.meses_d_servico / 12

class Professor(Funcionario):
    def __init__(self, nome, idade, salario, meses_d_servico, disciplina):
        super().__init__(nome, idade, salario, meses_d_servico)
        self.disciplina = disciplina
    
    def atividade(self):
        print(f"Professor(a) {self.nome} leciona {self.disciplina}")

p1 = Professor('Jurema', 55, 4200, 9, 'Português')
p1.atividade()


