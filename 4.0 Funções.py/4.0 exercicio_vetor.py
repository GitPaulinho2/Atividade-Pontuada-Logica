import os
os.system("clear")

quantidade_numeros = 5
lista_num = []

for i in range(quantidade_numeros):
        numero = int(input("Digite o seu número: "))
        if numero < 0:
            numero = 0
            lista_num.append(numero)

print("\n Números")
for i, numero in enumerate(lista_num, start=1):
    print(f"{i}: {numero}")       
