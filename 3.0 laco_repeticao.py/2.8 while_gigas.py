import os

os.system("clear")

# Exemplo de while

quantidade_notas = 3
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a sua 1ª nota:")) # 7 = aprovado
        
        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente.\n")
            break
        else:
            soma += nota
            break

media = soma / quantidade_notas


if media >= 7:
    resultado = "Aprovado!"
elif media >= 5:
    resultado = "Recuperação!"
else:
    resultado = "Reprovado!"

print(f"Média: {media}")
print(f"Resultado: {resultado}")
