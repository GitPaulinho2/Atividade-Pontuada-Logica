import os

os.system("clear")

# Exemplo de while


while True:
    nota = float(input("Informe sua nota:"))
    
    if nota < 0 or nota > 10:
       print("Nota inválida, tente novamente.\n")
    else:
        break

print(f"Sua nota: {nota}")
