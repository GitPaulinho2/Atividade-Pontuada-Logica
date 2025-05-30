import os

os.system("clear") # Limpa o terminal.

#Utilizando condicionais aninhados.
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print()
print(f"Média: {media}")

if media < 7:
    print("Reprovado")

else:
    resultado = "Reprovado!"
    
print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")
