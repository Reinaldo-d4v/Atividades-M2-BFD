"Crie uma classe Artista com um método apresentar() que imprime 'Sou artista'." 
"Crie uma classe Programador com um método apresentar() que imprime 'Sou programador'. "
"Depois crie uma classe PessoaMultiTalento que herda de ambas e veja qual método é chamado."
class Artista:
    
    def apresentacao(self):
        print('Sou artista')
class Programador:
    
    def apresentacao(self):
        print('Sou programador')
class PessoaMultiTalento(Artista, Programador):
    pass
PessoaMultiTalento().apresentacao()
