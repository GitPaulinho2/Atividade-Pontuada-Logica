import os

os.system("clear")

# Atividade de while e for
Quantidade_notas = 2 
soma = 0

for i in range(Quantidade_notas):
    while True:
        nota = float(input(f"Digite a sua {i+1}ª nota:"))

        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente.\n")
        else:
            soma += nota
            break

media = soma / Quantidade_notas

print(f"Média: {media}")