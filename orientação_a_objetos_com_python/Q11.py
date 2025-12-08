#.Use super() em todas as classes do exercício anterior para que
# os métodos sejam chamados em cadeia, 
# seguindo a MRO.
class Base:
    def apresentacao(self):
        pass 

class Artista(Base):
    def apresentacao(self):
        print('Sou artista')
        super().apresentacao() 
    
class Programador(Base):
    def apresentacao(self):
        print('Sou programador')
        super().apresentacao()

class PessoaMultiTalento(Artista,Programador):
    def apresentacao(self):
        print('Sou uma pessoa multi_talento')
        super().apresentacao()      
PessoaMultiTalento().apresentacao()
