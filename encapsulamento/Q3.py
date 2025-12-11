"Modifique a classe ContaBancaria para usar @property: "
"● O getter deve retornar o saldo. "
"● O setter deve permitir alterar o saldo somente se o valor for maior ou igual a zero."
class Conta_Bancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo
    @property 
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo (self, valor):
       if valor < 0:
            raise ValueError("O saldo não pode ser negativo")
       self.__saldo = valor

    def depositar(self, valor):
        if valor < 0:
             raise ValueError("O depósito deve ser positivo")
        if not isinstance (valor, (int,float)):
            raise TypeError('Tipo errado meu consagrado')
        self.__saldo += valor
        print(f"Depósito de R${valor} realizado")
        return self.__saldo
        
        
    def sacar(self, valor):
         if not isinstance (valor,(int,float)):
            raise TypeError('Tipo errado meu consagrado')
         if valor < 0:
             raise ValueError("O saque deve ser positivo")
         if self.__saldo < valor:
            raise ValueError ("Saldo insuficiente")
         self.__saldo -= valor
         print(f"Saque de R${valor} realizado")
         return self.__saldo
 
p1=Conta_Bancaria()
print(p1.depositar(5000))
print(p1.sacar(3000))
print(p1.saldo)
p1.saldo=5700
print(p1.saldo)
