#. Crie uma classe chamada Cachorro com os atributos nome e idade. 
# Adicione um método que exibe "Au au, meu nome é X e tenho Y anos". 
class Cachorro:
    def __init__(self, idade, nome):
        self.nome= nome
        self.idade = idade
    def metd_latir(self):
        print(f'Au au, meu nome é {self.nome} e tenho {self.idade} anos')
c=Cachorro(9,'Romeu')
c.metd_latir()