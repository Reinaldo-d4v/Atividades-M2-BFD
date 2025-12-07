#.Crie uma classe chamada Livro com atributos titulo, autor e ano. 
# Instancie três livros diferentes e mostre suas informações.
class Livro:
    def __init__(self, titulo,autor, ano):
        self.titulo= titulo
        self.autor=autor
        self.ano= ano

l1= Livro('As Tranças Do Rei Careca.', 'Wanderley.', 1923 )
l2= Livro('A Volta Dos Que Não Foram.', 'Lima Mei.', 2023)
l3= Livro('O Enxugador De Gelo.', 'Miro Tão.', 2000)

print(l1.titulo, l1.autor, l1.ano)
print(l2.titulo, l2.autor, l2.ano)
print(l3.titulo, l3.autor, l3.ano)