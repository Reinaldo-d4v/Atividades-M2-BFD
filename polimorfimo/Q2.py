"Crie uma classe Forma com o método area(). "
"Depois, crie duas classes filhas: "
"● Quadrado, que recebe o lado e calcula a área." 
"● Círculo, que recebe o raio e calcula a área . "
"● Crie uma função que recebe uma lista de formas geométricas e imprime a área de cada uma."
import math
class Forma:
    def __init__(self):
        pass
    def area(self):
       pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado=lado
    def area(self):
        return self.lado**2
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio=raio
    def area(self):
        return math.pi* (self.raio**2)

formas=[Quadrado(5), Circulo(5)]

def list_d_formas(formas):
    print([f.area() for f in formas])
list_d_formas(formas)

        