class Aluno:
    
    mediaAprovacao: float = 6.0
    
    def __init__(self, nome: str, matricula: str) -> None:
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        
    def Lanca_notas(self, valor: float) -> None:
        if valor >= 0  and valor <= 100 :
            self.notas.append(valor)
       
        
    def media(self) -> float:
        pass