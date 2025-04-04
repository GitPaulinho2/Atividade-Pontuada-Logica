import os
os.system("clear")

numero_informado = int(input("Digite o seu número: "))
def numero(numero_informado):
    if numero_informado % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")

numero(numero_informado)