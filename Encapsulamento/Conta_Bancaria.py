class ContaBancaria:
    def __init__(self, titular: str) -> None:
        self.titular = titular
        self.__saldo: float = 0.0
        
    def depositar(self, valor: float) -> None:
        self.__saldo += valor
    
    def saldo(self) -> float:
        return self.__saldo

conta1 = ContaBancaria("Isac")
conta1.depositar(100)

conta1.depositar(-500)

print(conta1.saldo)