import os

os.system("clear")

# Exemplo de while
idade = int(input("Digite sua idade:"))

while idade < 18:
    print("Não autorizado; \nSomente maiores de 18.\n")
    idade = int(input("Digite sua idade:"))


print("Acesso permitido.")
print("Fim.")