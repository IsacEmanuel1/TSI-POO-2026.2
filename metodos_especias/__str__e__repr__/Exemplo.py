class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        
    def __repr__(self) -> str:
        return f"Produto(nome=({self.nome!r}, preco={self.preco!r}))"
    
    def __str__(self) -> str:
        return f"{self.nome} - R$ {self.preco}"
    
P1 = Produto("cafe", 12.50)

print(P1)
print(P1.__repr__())
print(P1.__str__)

