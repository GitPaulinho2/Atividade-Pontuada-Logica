import os
import time

os.system("clear")



print("Contagem regressiva")
for i in range (0,1):  
   numero1 = int(input(f"Digite o seu número:"))
   numero2 = int(input(f"Digite o seu número:"))
   numero3 = int(input(f"Digite o seu número:"))
   numero4 = int(input(f"Digite o seu número:"))
   numero5 = int(input(f"Digite o seu número:"))
   resultado = numero1 + numero2 + numero3 + numero4 + numero5
   time.sleep(0.1)

print(f"Soma: {resultado}")