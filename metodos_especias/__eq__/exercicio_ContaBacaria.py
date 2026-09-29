class ContaBancaria:
    def __init__(self, titular: str, conta: int) -> None:
        self.titular = titular
        self.conta = conta
        self.saldo: float = 0.0
        
    def __str__(self) -> str:
        return f"Usuario: {self.titular}\nConta: {self.conta}\nSaldo: {self.saldo}"
    
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
        
    def sacar(self, valor: float) -> None:
        if valor <= self.saldo:
            self.saldo -= valor
    
    def __eq__(self, other: object):
        if not isinstance(other, ContaBancaria):
            return NotImplemented
        return self.titular == other.titular and self.conta == other.conta
        

usuaril1 = ContaBancaria("Isac", 20261148060040)
usuaril2 = ContaBancaria("Isac", 20261148060040)
usuaril3 = ContaBancaria("Luiza", 20261148060028)

print(usuaril1 == usuaril2)
print(usuaril1 == usuaril3)

usuaril1.depositar(500)
usuaril2.depositar(1000)
usuaril3.depositar(200)


print(usuaril1)
print()
print(usuaril2)
print()
print(usuaril3)
