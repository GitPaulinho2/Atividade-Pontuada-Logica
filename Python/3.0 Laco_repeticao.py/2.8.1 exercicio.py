import os

os.system("clear")

login_cadastrado = "admin"
senha_cadastrada = "123"
contador = 0

while True:
    login = input("Informe o seu login:")
    senha = input("Informe a sua senha:")

    if login_cadastrado == login and senha_cadastrada == senha:
        print("Bem vindo!")
        break
    else:
        print("Login ou senha incorretos, tente novamente.\n")
        contador += 1
        if contador == 3:
            print("Número de tentativas acima do permitido. (3)")
            break
