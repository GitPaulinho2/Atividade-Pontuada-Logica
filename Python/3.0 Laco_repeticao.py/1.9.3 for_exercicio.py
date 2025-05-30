import os

os.system("clear")


nota = 0

for i in range (1,4):  
   nota += float(input("Informe suas notas:"))

print(f"Média: {nota}")
if nota >= 7:
      print("Aprovado!")
elif nota < 4:
      print("Reprovado!")
else:
     nota == 4
     print("Recuperação!")
         