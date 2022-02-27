class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
    def __repr__(self):
        texto  = "Nome: {}\nIdade: {}\nE-mail: {}".format(
            self.nome,
            self.idade,
            self.email
        )
        return texto

    
class ContaCorrente:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
        
    def __repr__(self):
        texto = self.cliente.__repr__() + "Saldo: {}".format(
            self.__saldo
        )
        
    def saque(self, valor):
        if self.__saldo - valor >= 0:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente.')
            
    def deposito(self, valor):
        self.__saldo += valor
        
    def transferencia(self, other, valor):
        if self.__saldo - valor >= 0:
            self.__saldo -= valor
            other.__saldo += valor
        else:
            print('Saldo insuficiente.')

class ContaVip(ContaCorrente):
    def __init__(self, cliente, saldo=0, cheque_especial=0):
        super().__init__(cliente, saldo)
        self.cheque_especial = cheque_especial
    
    def saque(self, valor):
        if((self.saldo + self.cheque_especial) - valor >= 0):
            self.deposito(-valor)
        else:
            print('Saldo insuficiente.')
            
    def transferencia(self, other, valor):
        if((self.saldo+self.cheque_especial) - valor >= 0):
            self.deposito(-valor)
            other.deposito(valor)
        else:
            print('Saldo insuficiente.') 
            