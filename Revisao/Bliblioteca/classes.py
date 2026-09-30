from erros import ErroDeBliblioteca, LivroIndisponivelError, LivroNaoEncontradoError

class Livro: 
    def __init__(self, titulo: str, ano: int) -> None:
        self.titulo = titulo
        self.ano = ano
        self.disponivel: bool = True
        
    def __str__(self) -> str:
        status = "Disponivel" if self.disponivel else "emprestado"
        return f"{self.titulo} ({self.ano}) - {status}"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Livro):
            return NotImplemented
        return self.titulo == other.titulo and self.ano == other.ano
    
class Bliblioteca:
    def __init__(self) -> None:
        self._acervo: list[Livro] = [] #tipoando para essa lista receber somente objetos da classe livro
        
    def cadastrar(self, livro: Livro) -> None:
        self._acervo.append(livro)
        
    def _buscar(self, titulo: str) -> Livro: # Esse metodo so pode ser usado dentro da clsse Bliblioteca
        for livro in self._acervo:
            if livro.titulo == titulo:
                return livro
        raise LivroNaoEncontradoError(titulo)
    
    def emprestar(self, titulo: str) -> None:
        livro = self._buscar(titulo)
        if not livro.disponivel:
            raise LivroIndisponivelError(titulo)
        livro.disponivel = False
        
    def devolver(self, titulo: str) -> None:
        self._buscar(titulo).disponivel = True
        
    def disponiveis(self) -> object:
        for livro in self._acervo:
            if livro.disponivel:
                print(livro)