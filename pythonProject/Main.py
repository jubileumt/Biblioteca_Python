from Pessoa import Pessoa
from Livro import Livro
from Biblioteca import Bibioteca

print("------Bem vindo à biblioteca digital------")

while True:
    print("1- Para registrar usuário.")
    print("2- Para buscar usuário.")
    print("3- Para registrar livro.")
    print("4- Para buscar livro.")
    print("5- Alugar livro.")
    print("6- Devolver livro.")
    print("7- Para sair.")

    opc = int(input("Escolha: "))

    if opc == 1:
        nome = input("Qual o seu nome? ")
        idadestr = input("Qual a sua idade? ")
        idade = int(idadestr)
        cpf = input("Qual o seu CPF? ")
        email = input("Qual o seu email? ")
        cidade = input("Qual a sua cidade? ")

        pessoa = Pessoa(nome, idade, cpf, email, cidade)
        pessoa.adicionar_usuario()

    if opc == 2:
       cpf = input("Qual o seu CPF? ")
       pessoa = Pessoa.buscar_usuario(cpf)
       if pessoa:
        print()
        print("Dados do usuario")
        print("Nome: " + pessoa.nome_usuario)
        print(f"Idade: {pessoa.idade}")
        print("CPF: " + pessoa.cpf)
        print("Email: " + pessoa.email)
        print("Cidade: " + pessoa.cidade)

       else:print("Usuario não encontrado!")

       if pessoa.livro_emprestado:
           print()
           print("Dados do livro alugado")
           print("Nome do livro pego: " + pessoa.livro_emprestado.nome)
           print("Autor do livro pego: " + pessoa.livro_emprestado.autor)
           print("Genero do livro pego: " + pessoa.livro_emprestado.genero)
           print("ISBN do livro pego: " + pessoa.livro_emprestado.ISBN)
           print()

    if opc == 3:
        nome = input("Qual o nome do livro? ")
        autor = input("Qual o autor do livro? ")
        isbn = input("Qual o ISBN do livro? ")
        genero = input("Qual o genero do livro? ")

        livro = Livro(nome, autor, isbn, genero)
        livro.Inluir_Livro()

    if opc == 4:
        isbn = input("Qual o ISBN do livro que deseja achar? ")
        livro_achado = Livro.buscar_Livro(isbn)

        if livro_achado:
         print("Nome: " + livro_achado.nome)
         print("Autor: " + livro_achado.autor)
         print("ISBN: " + livro_achado.ISBN)
         print("Genero: " + livro_achado.genero)
         if livro_achado.disponivel  == True:
             print("Livro disponivel para emprestimo ")
             print()
         else :
             print("Livro não disponivel para emprestimo")
             print()

    if opc == 5:
       cpf = input("Qual o seu CPF?")
       usuario_achado = Pessoa.buscar_usuario(cpf)

       if usuario_achado:
          isbn = input("Qual o ISBN do livro? ")
          livro_achado = Livro.buscar_Livro(isbn)
          if livro_achado:
              Bibioteca.pegar_livro_emprestado(usuario_achado,livro_achado)
              print("Livro alugado com sucesso!")


    if opc == 6:
       cpf = input("Qual o seu CPF?")
       usuario_achado = Pessoa.buscar_usuario(cpf)

       if usuario_achado:
          livro_achado = Livro.buscar_Livro(usuario_achado.livro_emprestado.ISBN)
          if livro_achado:
              Bibioteca.devolver_livro_emprestado(usuario_achado,livro_achado)
              print("Livro devolvido com sucesso!")

    elif opc == 7:
         print("Saindo...")
         break


