"Crie uma classe Produto com atributos privados __nome e __preco." 
"O nome só pode ser lido, não alterado."
"● O preço pode ser lido e alterado, mas não pode ser negativo." 
"● Use @property e @setter."
class Produto:
    def __init__(self, nome:str,preco:float):
        self.__nome=nome
        self.__preco= preco
  
    @property
    def nome(self):
        return self.__nome
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, preco):
           if preco < 0:
            raise ValueError ("Valor negativo, digite novamnete")
           self.__preco = preco 
p1= Produto('Maçã', 2.5)
p2=Produto('Pêra', 6)
print(f'nome:{p1.nome} \npreço:{p1.preco}')
print(f'nome:{p2.nome} \npreço:{p2.preco}')
p1.preco=5000
print(f'nome:{p1.nome} \npreço:{p1.preco}')

        


            
    
