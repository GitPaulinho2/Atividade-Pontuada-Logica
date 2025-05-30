import os

os.system("clear")


primeiro_numero = float(input("Informe seu primeiro número:"))
segundo_numero = float (input("Informe seu segundo: número:"))
terceiro_numero = float (input("Informe seu terceiro número:"))



if primeiro_numero + segundo_numero > terceiro_numero:
    print("A soma do primeiro com o segundo número tem o resultado maior que o terceiro número.")
elif primeiro_numero + segundo_numero < terceiro_numero:
    print("A soma do primeiro e do segundo número tem o resultado menor que o terceiro")
else: 
    print("A soma do primeiro e do segundo número tem o resultado igual ao terceiro")