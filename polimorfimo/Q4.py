" Crie uma classe Veiculo com o método mover()." 
"Depois crie: "
"● Carro, que imprime 'Dirigindo...'." 
"● Bicicleta, que imprime 'pedalando...'. "
"● Avião, que imprime 'Voando...'. "
"● Faça um programa que receba uma lista de veículos e use um loop para chamar o método mover()" 
"de cada um."
class Veiculo:
    def mover(self):
        print('')
class Carro(Veiculo):
    def mover(self):
        print('Dirigindo')
class Aviao(Veiculo):
    def mover(self):
        print('Voando')
class Bicicleta(Veiculo):
    def mover (self):
        print('Pedalando')
transporte=[Carro(), Aviao(), Bicicleta()]
for f in transporte:
    f.mover()