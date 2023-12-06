import sqlite3
from crud import *

conn = sqlite3.connect('livraria.db')
cursor = conn.cursor()

def menu():
    while True:
        print("\n--- BEM VINDO! ---")
        print("1- Adicionar Livro")
        print("2- Buscar Livro por ID")
        print("3- Atualizar Livro por ID")
        print("4- Excluir Livro por ID")
        print("5- Listar Todos os Livros")
        print("6- Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            title = input("Digite o título do livro: ")
            author = input("Digite o autor do livro: ")
            genre = input("Digite o gênero do livro: ")
            isbn = input("Digite o ISBN do livro: ")
            create_book(title, author, genre, isbn)
        elif opcao == '2':
            id_busca = int(input("Digite o ID do livro a ser buscado: "))
            select_book(id_busca)
        elif opcao == '3':
            id_atualizar = int(input("Digite o ID do livro a ser atualizado: "))
            title = input("Digite o novo título do livro: ")
            author = input("Digite o novo autor do livro: ")
            genre = input("Digite o novo gênero do livro: ")
            isbn = input("Digite o novo ISBN do livro: ")
            update_book(id_atualizar, title, author, genre, isbn)
        elif opcao == '4':
            id_excluir = int(input("Digite o ID do livro a ser excluído: "))
            delete_book(id_excluir)
        elif opcao == '5':
            cursor.execute('SELECT * FROM book')
            livros = cursor.fetchall()
            if livros:
                print("\n--- Lista de Livros ---")
                for livro in livros:
                    print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Gênero: {livro[3]} | ISBN: {livro[4]}")
            else:
                print("Não há livros cadastrados.")
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")