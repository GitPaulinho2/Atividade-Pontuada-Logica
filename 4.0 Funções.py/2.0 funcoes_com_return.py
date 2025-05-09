import os
os.system("clear")

def somar (n1,n2):
    calcular = n1 + n2
    return calcular

def subtrair (n1,n2):
    calcular = n1 - n2
    return calcular

def dividir (n1,n2):
    calcular = n1 / n2
    return calcular

def multiplicar (n1,n2):
    calcular = n1 * n2
    return calcular
n1 = int(input("Digite seu primeiro número:"))
n2 = int(input("Digite seu segundo número:"))


soma = somar(n1, n2)
subtracao = subtrair (n1,n2)
multiplicacao = multiplicar (n1,n2)
divisao = dividir (n1,n2)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")