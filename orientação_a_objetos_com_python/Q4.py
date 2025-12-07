#Adicione à classe Carro um método chamado dirigir()
# que imprime "O carro está em movimento". 
class Carro:
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo= modelo
    def dirigir(self):
        print('O carro esta em movimento')

carro = Carro('BYD', 'Seal' )
carro1 = Carro('Toyota', 'Etios')

print(carro.marca, carro.modelo)
print(carro1.marca, carro1.modelo)
carro1.dirigir()