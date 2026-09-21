
# 6 — Classe Aluno

class Aluno:
    """Representa um aluno com nome, matrícula e lista de notas."""

    MEDIA_APROVACAO: float = 6.0

    def __init__(self, nome: str, matricula: str) -> None:
        self.nome: str = nome
        self.matricula: str = matricula
        self.notas: list[float] = []

    def lancar_nota(self, valor: float) -> None:
        """Adiciona uma nota à lista de notas do aluno."""
        self.notas.append(valor)

    def media(self) -> float:
        """Retorna a média das notas (0.0 se ainda não há notas)."""
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def aprovado(self) -> bool:
        """Retorna True se a média for maior ou igual a 6."""
        return self.media() >= self.MEDIA_APROVACAO

    def __str__(self) -> str:
        return f"{self.nome} ({self.matricula}) — média {self.media():.1f}"


# 7 — Criar 3 alunos, lançar notas e imprimir apenas os aprovados

def questao_7() -> None:
    ana = Aluno("Ana", "20261234")
    bruno = Aluno("Bruno", "20261235")
    carla = Aluno("Carla", "20261236")

    for nota in (8.0, 7.0, 7.5, 7.5):
        ana.lancar_nota(nota)

    for nota in (4.0, 5.5, 6.0):
        bruno.lancar_nota(nota)

    for nota in (6.0, 6.0, 9.0):
        carla.lancar_nota(nota)

    alunos: list[Aluno] = [ana, bruno, carla]

    print("Alunos aprovados:")
    for aluno in alunos:
        if aluno.aprovado():
            print(aluno)



# 8 — Classe Retangulo

class Retangulo:
    """Retângulo definido por base e altura."""

    def __init__(self, base: float, altura: float) -> None:
        self.base: float = base
        self.altura: float = altura

    def area(self) -> float:
        """Retorna a área do retângulo."""
        return self.base * self.altura

    def perimetro(self) -> float:
        """Retorna o perímetro do retângulo."""
        return 2 * (self.base + self.altura)

    def __eq__(self, outro: object) -> bool:
        """Dois retângulos são iguais se têm as mesmas dimensões."""
        if not isinstance(outro, Retangulo):
            return NotImplemented
        return self.base == outro.base and self.altura == outro.altura

    def __hash__(self) -> int:
        return hash((self.base, self.altura))

    def __str__(self) -> str:
        return f"Retangulo({self.base} x {self.altura})"



# 9 — Classe Data

class Data:
    """Data representada por dia, mês e ano."""

    def __init__(self, dia: int, mes: int, ano: int) -> None:
        self.dia: int = dia
        self.mes: int = mes
        self.ano: int = ano

    @classmethod
    def de_texto(cls, texto: str) -> "Data":
        """Cria uma Data a partir de uma string no formato 'dd/mm/aaaa'."""
        dia, mes, ano = texto.split("/")
        return cls(int(dia), int(mes), int(ano))

    @staticmethod
    def bissexto(ano: int) -> bool:
        """Retorna True se o ano for bissexto."""
        return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

    def __str__(self) -> str:
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"



# Testes

if __name__ == "__main__":
    print("---  7 ---")
    questao_7()

    print("\n--- 8 ---")
    r1 = Retangulo(3, 4)
    r2 = Retangulo(3, 4)
    r3 = Retangulo(2, 5)
    print(r1, "área:", r1.area(), "perímetro:", r1.perimetro())
    print("r1 == r2:", r1 == r2)
    print("r1 == r3:", r1 == r3)

    print("\n--- 9 ---")
    data = Data.de_texto("9/8/2026")
    print(data)
    print(Data(1, 1, 2026))
    print("2024 é bissexto?", Data.bissexto(2024))
    print("1900 é bissexto?", Data.bissexto(1900))
    print("2000 é bissexto?", Data.bissexto(2000))