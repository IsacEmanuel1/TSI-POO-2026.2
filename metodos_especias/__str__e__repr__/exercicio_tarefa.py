class Tarefa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.estado: bool = False
        self.lista_tarefas = []
    
    def __str__(self) -> str:
        return f"Tarefas cadastrada: {self.nome} -> Situação: {self.estado}"
    
    def __repr__(self) -> None:
        return f"Tarefa({self.nome}, {self.estado})"
    
    
    
tareafa1 = Tarefa("Estudar POO")
tarefa2 = Tarefa("Fazer execicio de POO")

print(tareafa1)
print(repr(tarefa2))