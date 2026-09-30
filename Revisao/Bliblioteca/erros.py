class ErroDeBliblioteca(Exception): pass
class LivroIndisponivelError(ErroDeBliblioteca): pass
class LivroNaoEncontradoError(ErroDeBliblioteca): pass
