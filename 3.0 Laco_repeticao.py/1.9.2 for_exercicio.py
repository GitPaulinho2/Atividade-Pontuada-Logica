import os
import time

os.system("clear")


nota = 0
soma = 0

for i in range (1,5):  
   nota += float(input("Informe suas notas:"))
               
   media = soma / 4
print(f"Média: {nota}")