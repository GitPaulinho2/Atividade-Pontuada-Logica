import os
os.system("clear")

numero_informado = int(input("Digite o seu número: "))
def numero (numero_informado):
    if numero_informado > 0:
        print("O número é positivo")
    elif numero_informado == 0:
        print("O número é neutro")
    else:
        print("O número é negativo")
        
    
numero(numero_informado)
        