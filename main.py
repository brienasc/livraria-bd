from crud import create_user
from login import *
from menu import *

while True:
    print("------- LIVRARIA INDIGO -------")
    print("1- Cadastrar Usuário")
    print("2- Login")
    print("3- Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        username = input("Digite o username: ")
        password = input("Digite a senha: ")
        create_user(username, password)
    elif opcao == 2:
        username = input("Digite o username: ")
        password = input("Digite a senha: ")
        if login(username, password):
            print("Login realizado com sucesso!")
            menu()
        else:
            print("Credenciais inválidas. Tente novamente.")
    elif opcao == 3:
        break
    else:
        print("Opção Inválida. Tente Novamente!")