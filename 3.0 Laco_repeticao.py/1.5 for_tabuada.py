import os
import time

os.system("clear")


numero = int(input("Digite um número para a tabuada:"))

print(f"Tabuada do número: {numero}")
for i in range(1, 11):
    print (f"{numero} x {i} = {i*numero}")
    time.sleep(0.1) # espera 1 segundo

