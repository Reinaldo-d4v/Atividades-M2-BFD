"Crie uma classe Pessoa com os atributos: "
"● nome (público) "
"● _anoNasceu (protegido) "
"Instancie um objeto e mostre que é possível acessar _idade, mas que não é recomendado."
from datetime import date
class Pessoa:
    def __init__(self, nome, anoNasceu):
        self.nome= nome
        self._anoNasceu= anoNasceu
        self._idade= date.today().year - anoNasceu
p1= Pessoa('Lira', 2000)
print(p1.nome)
print(p1._idade)#Não recomendado
