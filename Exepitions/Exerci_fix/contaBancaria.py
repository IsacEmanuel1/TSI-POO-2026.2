class SaldoInsuficienteError(Exception):
    """
    Saque Maior que o Disponivel!
    """

class ContaBancaria:
    def __init__(self, titular: str) -> None:
        self.titular: float = titular
        self.saldo = 0.0

    def Sacar(self, valor: float) -> None:
        if valor >= 0:
            raise ValueError("O valor deve ser positivo!")
        elif valor < self.saldo:
            raise SaldoInsuficienteError(f"Saldo: {self.saldo}" f"Valor de Saque: {valor:.2f}")
        self.saldo -= valor

isac = ContaBancaria("isac")
try:
    isac.Sacar(0)
except SaldoInsuficienteError as erro:
    print("Operação Negada! {erro}")
    
