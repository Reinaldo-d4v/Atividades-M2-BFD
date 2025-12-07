# Na classe Cachorro, adicione um método aniversario()
# que aumenta a idade em 1 e mostre o novo valor.
class Cachorro:
    def __init__(self, idade, nome):
        self.nome= nome
        self.idade = idade
    def aniversario(self):
        self.idade+=1
    def metd_latir(self):
        print(f'Au au, meu nome é {self.nome} e tenho {self.idade} anos')
    

c=Cachorro(9,'Romeu')
c.aniversario()
c.metd_latir()
