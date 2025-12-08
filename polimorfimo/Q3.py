" Crie uma classe Funcionario com um método salario(). "
"Depois crie duas subclasses: "
"● Gerente, que retorna 5000. "
"● Estagiario, que retorna 1500. "
"● Crie uma lista com funcionários diferentes e mostre o salário de cada um. "
class Funcionario:
    def salario(self):
        return None
class Gerente(Funcionario):
    def salario(self):
        return 5000
class Estagiario(Funcionario):
    def salario(self):
        return 1500

funcionarios = [Estagiario(), Gerente()]

for f in funcionarios:
    print(f.salario())
