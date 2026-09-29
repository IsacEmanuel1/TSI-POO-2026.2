"""
| Operador | Método        |
| -------- | ------------- |
| `a == b` | `a.__eq__(b)` |
| `a != b` | `a.__ne__(b)` |
| `a < b`  | `a.__lt__(b)` |
| `a <= b` | `a.__le__(b)` |
| `a > b`  | `a.__gt__(b)` |
| `a >= b` | `a.__ge__(b)` |

"""

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos"
    
    def __repr__(self) -> str:
        return f"Pessoa({self.nome!r}, {self.idade!r})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.nome == other.nome and self.idade == other.idade
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Pessoa):
            return NotImplemented
        return self.idade < other.idade
    
    
pessoa1 = Pessoa("Isac", 19)
pessoa2 = Pessoa("Vitoria", 24)
pessoa3 = Pessoa("Isac", 19)

print(pessoa1 == pessoa2)
print(pessoa1 == pessoa3)
print(pessoa1 < pessoa2)

pessoas = [pessoa1, pessoa2, pessoa3]
pessoas_ordenasdas = sorted(pessoas)

for pessoa in pessoas_ordenasdas:
    print(pessoa)
    