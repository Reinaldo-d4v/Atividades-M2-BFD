# Crie uma classe ContaBancaria com os atributos titular e saldo. 
# Adicione métodos para depositar(valor) e sacar(valor). 
# Garanta que o saldo não fique negativo.
class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular=titular
        self.saldo=saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Novo deposito concluido, saldo atual:{self.saldo}')
    
    def sacar(self, valor, ):
        if self.saldo >= valor:
          self.saldo-=valor
          print(f'Novo saque concluido, saldo atual:{self.saldo}')

        else:
          print('Saldo insuficiente')
conta= Conta_Bancaria('Rooney',4000)
conta.depositar(1000)
conta.sacar(2000)
conta.sacar(10000)

        
