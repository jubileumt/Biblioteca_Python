from Pessoa import Pessoa
from Livro import Livro
from abc import ABC, abstractmethod

class Bibioteca:
     def pegar_livro_emprestado(pessoa,livro):
         print()
         pessoa.livro_emprestado = livro
         livro.disponivel = False
         livro.dono = pessoa

     def devolver_livro_emprestado(pessoa,livro):
          print()
          pessoa.livro_emprestado = None
          livro.disponivel = True
          livro.dono = None
