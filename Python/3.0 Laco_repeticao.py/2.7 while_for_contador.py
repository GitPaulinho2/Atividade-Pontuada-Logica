import os

os.system("clear")



login_cadastrado = "diego"
senha_cadastrada = "123"
contador = 0

while True:
    login = input("Informe seu login:")
    senha = input("Informe sua senha:")
    if login_cadastrado == login and senha_cadastrada == senha:
        print("Bem vindo calabreso")
        break
    else:
        print("Acesso negado. \nTente novamente\n")
        contador += 1
        if contador == 3:
            print("Número de tentativas acima do permitido (3)")
            break