import os
import time

os.system("clear")


nota = 0
soma = 0

for i in range (1,4):  
   nota += float(input("Informe suas notas:"))
   media = soma / 3
print(f"Média: {nota}")

if media >= 7:
      print("Aprovado!")
elif media < 4:
      print("Reprovado!")
else:
     media == 4
     print("Recuperação!")

         