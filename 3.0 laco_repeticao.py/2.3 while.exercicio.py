import os

os.system("clear")

# Exemplo de while



while True:
    nota1 = float(input("Informe sua nota:"))
    nota2 = float(input("Informe sua nota:"))

    if nota1 < 0 or nota1 > 10:
       print("Nota inválida, tente novamente.\n")
    else:
        break
while True:

    if nota2 < 0 or nota2 > 10:
       print("Nota inválida, tente novamente.\n")
    else:
        break
    
media = (nota1 + nota2) / 2
print(f"Média do Aluno: {media}")