import os 

os.system("clear")

preco_alcool = 3.79
preco_gasolina = 6.59

tipo_combustivel = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ")
litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))

if tipo_combustivel == "A":
    preco_total = litros_vendidos * preco_alcool
    if litros_vendidos <= 25:
        desconto = preco_total * 0.02  
    else:
        desconto = preco_total * 0.04  

elif tipo_combustivel == "G":
    preco_total = litros_vendidos * preco_gasolina
    if litros_vendidos <= 25:
        desconto = preco_total * 0.03 
    else:
        desconto = preco_total * 0.05 
else:
    print("Tipo de combustível inválido!")
    desconto = 0
    preco_total = 0

valor_a_pagar = preco_total - desconto

if preco_total > 0:
    print(f"\nValor total sem desconto: R$ {preco_total:.2f}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")