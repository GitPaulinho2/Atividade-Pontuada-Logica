import os

os.system("clear")

pares = 0
impares = 0
soma_pares = 0
soma = 0
quantidade_geral = 0

while True:
    numero = int(input("Digite um número:"))
    if numero == 0:
        break
    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1

    soma += numero
    quantidade_geral += 1

if quantidade_geral > 0:
    media_pares = soma_pares / pares
    media_geral = soma / quantidade_geral
   
    print(f"Quantidade de pares: {pares}")
    print(f"Quantidade de imapares: {impares}")
    print(f"Méda de pares: {media_pares}")
    print(f"Méda geral: {media_geral}")

    
else:
    print("\nNão foram informados números necessários para a operação!")