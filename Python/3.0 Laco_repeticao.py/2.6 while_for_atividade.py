import os

os.system("clear")

login_cadastrado = "diego"
senha_cadastrada = "123"


for i in range (3):
        login = input("Informe seu login:")
        senha = input("Informe sua senha:") 
        if login_cadastrado == login and senha_cadastrada == senha:
            print("Bem vindo!")
            break
        else:
            print("Login ou senha incorretos!")
        if i == 2:
            print(f"Número de tentativas acima do permitido ({i+1}).\n")


print()
print(f"Login: {login_cadastrado}")
print(f"Senha: {senha_cadastrada}")