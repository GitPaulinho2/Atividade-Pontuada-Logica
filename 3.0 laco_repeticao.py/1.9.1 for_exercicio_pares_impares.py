import os
import time

os.system("clear")

pares = 0
impares = 0

for i in range(5):
    numero = int(input("Digite um número:"))
    if numero % 2 == 0:
      pares += 1
    else:
       impares += 1




print(f"Números impares: {impares}")
print(f"Números pares: {pares}")



