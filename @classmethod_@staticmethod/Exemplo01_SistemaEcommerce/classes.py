from datetime import datetime

class Produto:
    # Atributo de classe: contador global de produtos criados
    total_produtos = 0
    # Atributo de classe: taxa de imposto padrão da loja
    TAXA_IMPOSTO = 0.10

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco
        Produto.total_produtos += 1  # atualiza estado da classe

    # ---- MÉTODO DE INSTÂNCIA (para comparação) ----
    def preco_com_imposto(self) -> float:
        # Precisa de 'self' pois depende do preço DESTA instância
        return self.preco * (1 + Produto.TAXA_IMPOSTO)

    # ---- CLASSMETHOD: Construtor alternativo ----
    @classmethod
    def criar_a_partir_de_string(cls, dados: str):
        """
        Cria um Produto a partir de uma string 'nome-preco'.
        Usa 'cls' para poder ser herdado corretamente por subclasses
        (se uma subclasse chamar isso, 'cls' será a subclasse, não Produto).
        """
        nome, preco = dados.split("-")
        return cls(nome, float(preco))  # cls() == Produto() (ou subclasse)

    # ---- CLASSMETHOD: acessa/modifica estado da classe ----
    @classmethod
    def alterar_taxa_imposto(cls, nova_taxa: float):
        """Modifica um atributo compartilhado por TODAS as instâncias."""
        cls.TAXA_IMPOSTO = nova_taxa

    # ---- STATICMETHOD: utilitário sem relação com estado ----
    @staticmethod
    def validar_preco(preco: float) -> bool:
        """
        Não precisa de 'self' nem 'cls' — é uma regra de negócio
        genérica que só está aqui por coesão lógica (faz sentido
        estar dentro de Produto, mas não acessa nada da classe).
        """
        return preco > 0

    @staticmethod
    def gerar_timestamp_criacao() -> str:
        """Outro utilitário: não depende de nenhum dado do Produto."""
        return datetime.now().isoformat()


# --- Uso ---
p1 = Produto("Notebook", 3000)
p2 = Produto.criar_a_partir_de_string("Mouse-150")  # construtor alternativo

print(Produto.validar_preco(-10))          # False — chamado direto na classe
print(p1.preco_com_imposto())              # 3300.0 — depende da instância

Produto.alterar_taxa_imposto(0.15)          # afeta TODAS as instâncias
print(p2.preco_com_imposto())               # já usa a nova taxa: 172.5

print(Produto.total_produtos)               # 2