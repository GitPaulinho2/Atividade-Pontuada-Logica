import os 

os.system("clear")

login_cadastrado = "aluno"
senha_cadastrada = "123"

login = input("Digite seu login:")
senha = input("Digite sua senha:")

if login_cadastrado == login and senha_cadastrada == senha:
    print("Bem vindo!")

else:
    print("Login ou senha invalidos!")