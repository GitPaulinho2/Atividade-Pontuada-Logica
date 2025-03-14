import os
import time

os.system("clear")

numero = int(input("Digite o seu número para a contagem:"))


print("Contagem regressiva")
for i in range (numero, 0, -1): # se fizer (0, numero) começa a contar do 0
    print(f"{i}")
    time.sleep(1) # espera 1 segundo

