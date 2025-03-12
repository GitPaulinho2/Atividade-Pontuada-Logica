import os 

os.system("clear")


primeira_nota = float(input("Digite a sua primeira nota:"))
segunda_nota = float(input("Digite a sua segunda nota:"))

media = primeira_nota + segunda_nota

print()
print(f"Nota final: {media}")
if media == 5:
    print("Recuperação!")
elif media < 5:
    print("Reprovado!")
else:
    print("Aprovado!")    



