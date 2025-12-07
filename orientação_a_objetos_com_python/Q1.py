# Crie uma classe chamada Carro com os atributos marca e modelo. 
# Depois crie dois objetos diferentes dessa classe e imprima os valores.
class Carro:
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo= modelo

carro = Carro('BYD', 'Seal' )
carro1 = Carro('Toyota', 'Etios')

print(carro.marca, carro.modelo)
print(carro1.marca, carro.modelo)