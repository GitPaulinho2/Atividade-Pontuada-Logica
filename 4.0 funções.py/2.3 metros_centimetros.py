import os
os.system("clear")

metros = float(input("Digite quantos metros você quer: "))

def redu():
     calcular = metros * 100
     return calcular

calcular = redu()

print(f"Convertendo {metros:.2f} metros em centimetros: {calcular:.2f}")