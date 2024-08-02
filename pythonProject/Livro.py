
class Livro:

    Livraria = []

    def __init__(self, nome,genero,isbn,autor):
        self.nome = nome
        self.genero = genero
        self.ISBN = isbn
        self.autor = autor
        self.disponivel = True
        self.dono = None

    @staticmethod
    def verificar_livro(isbn):
        if any(livro.ISBN == isbn for livro in Livro.Livraria):
            print("Livro repetido!")
            print()
            return False
        return True

    def Inluir_Livro(self):
        resultado = self.verificar_livro(self.ISBN)
        if resultado:
            Livro.Livraria.append(self)
            print("Livro incluido na biblioteca digital com sucesso!")
            print()

    @staticmethod
    def buscar_Livro(isbn):
     for livro in Livro.Livraria:
        if livro.ISBN == isbn:
            return livro
     return None