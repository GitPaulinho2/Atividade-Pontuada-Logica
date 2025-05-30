import os
import time

os.system("clear")


soma = 0
for i in range (1,6):  
   numero = int(input("Digite um número:"))
 #  soma = soma + numero
   soma += numero

print(f"Soma: {soma}")