class Tarefa: 
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade

    def __str__(self):
        return f"Tarefa: {self.descricao}, Prioridade: {self.prioridade}"

    def __repr__(self):
        pass