import os

os.system("clear")

login_cadastrado = "diego"
senha_cadastrada = "123"

while True:
    login = input("Informe o seu username:")
    senha = input("Informe sua senha:")

    if login_cadastrado == login and senha_cadastrada == senha:
        print("Bem vindo!")
        break
    else:
        print("Login ou senha inválidos!")
    
print(f"Login: {login}")
print(f"Senha: {senha}")
             


    