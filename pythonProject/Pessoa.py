from typing import Optional
from Livro import Livro
class Pessoa:

    todos_usuarios = []

    def __init__(self, nome, idade, cpf, email, cidade):
        self.nome_usuario = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.cidade = cidade
        self.livro_emprestado: Optional[Livro] = None
    @staticmethod
    def verificacoes(idade, cpf):
        if idade < 18:
            print("Precisa ser maior de idade!")
            print()
            return False
        if any(pessoa.cpf == cpf for pessoa in Pessoa.todos_usuarios):
            print("CPF já registrado!")
            print()
            return False
        return True

    def adicionar_usuario(self):
        resultado = Pessoa.verificacoes(self.idade, self.cpf)
        if resultado:
            Pessoa.todos_usuarios.append(self)
            print(f"Usuário {self.nome_usuario} adicionado com sucesso!")
            print()
    @staticmethod
    def buscar_usuario(cpf):
        for pessoa in Pessoa.todos_usuarios:
            if pessoa.cpf == cpf:
                return pessoa
            else: print("Usuario não encontrado!")
        return None
