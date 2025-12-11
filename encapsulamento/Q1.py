" Crie uma classe ContaBancaria com um atributo privado __saldo. "
"Inicialize o saldo com 0. "
"● Crie métodos depositar(valor) e sacar(valor)." 
"● Crie também um método ver_saldo() que retorne o valor do saldo."
class Conta_Bancaria:
    def __init__(self, saldo=0):
        self.__saldo = saldo
        
    def depositar(self, valor):
        if not isinstance (valor,(int,float)):
            raise TypeError("Digite um número por favor")

        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado")
            return self.__saldo
        else:
            raise ValueError("O depósito deve ser positivo")
        

    def sacar(self, valor):
         if not isinstance (valor,(int,float)):
            raise TypeError("Digite um número por favor")
         if self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado")
            return self.__saldo
         else:
            raise ValueError("Saldo insuficiente")
        
    def ver_saldo(self):
        return self.__saldo


p1 = Conta_Bancaria()
print(p1.depositar(1500))
print(p1.sacar(100))
print(p1.ver_saldo())

