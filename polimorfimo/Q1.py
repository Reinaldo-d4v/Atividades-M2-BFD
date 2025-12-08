"Crie uma classe Animal com o método falar(). "
"Depois, crie as classes Cachorro e Gato que herdam de Animal e implementam falar() de forma" 
"diferente:" 
"● O cachorro deve imprimir 'Au au!' "
"● O gato deve imprimir 'Miau!'" 
"● Crie uma lista com vários animais e percorra a lista chamando falar() em cada um. "
class Animal: 
    def falr(self):
        pass
class Cachorro(Animal):
    def falr(self):
        print('Au au!!')
class Gato(Animal):
    def falr(self):
        print('Miau!')
animais= [Cachorro(), Gato(), Cachorro(), Gato()]
for falr in animais:
    falr.falr()

