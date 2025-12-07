#Crie uma classe Funcionario que herda de Pessoa e adiciona salario.
# Crie um método que calcula o 13º salário (um salário extra). 
class Pessoa:
    def __init__ (self,nome,idade):
        self.nome= nome
        self.idade= idade

class Funcionario(Pessoa):
    def __init__(self,nome, idade, salario, meses_d_servico):
        super().__init__(nome, idade)
        self.salario= salario
        self.meses_d_servico=meses_d_servico
        self.decimo_terceiro= None
    
    def calc_decimo_3(self):
        self.decimo_terceiro= self.salario * self.meses_d_servico/12

p1= Funcionario('Xispirinu', 55, 3900, 9)
p1.calc_decimo_3()
print(f'Funcionário: {p1.nome}\nidade: {p1.idade}\nsalario: {p1.salario}\nDecimo_3: {p1.decimo_terceiro}\nQ.de meses trabalhado: {p1.meses_d_servico}')

