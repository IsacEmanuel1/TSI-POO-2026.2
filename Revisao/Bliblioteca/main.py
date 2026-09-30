from classes import Livro, Bliblioteca
from erros import LivroIndisponivelError, LivroNaoEncontradoError, ErroDeBliblioteca

biblio = Bliblioteca()

biblio.cadastrar(Livro("Dom Casmurro", 1899))
biblio.cadastrar(Livro("Vidas Secas", 1938))
biblio.cadastrar(Livro("Memórias póstumas de Brás Cubas", 1881))

biblio.disponiveis()

try:
    biblio.emprestar("Dom Casmurro")
    biblio.emprestar("Dom Casmurro")
except LivroIndisponivelError as error:
    print(f"Livro Indisponivel: {error}")
except LivroNaoEncontradoError as error:
    print(f"Livro não Encontrado: {error}")

print("\nPos Emprestimo:\n")
biblio.disponiveis()

try:
    biblio.emprestar("Nao existe")
except LivroIndisponivelError as error:
    print(f"Livro Indisponivel: {error}")
except LivroNaoEncontradoError as error:
    print(f"Livro não Encontrado: {error}")
    
biblio.devolver("Dom Casmurro")

print("\nPos Devolução:\n")
biblio.disponiveis()