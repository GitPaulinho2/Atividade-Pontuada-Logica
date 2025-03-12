import os

os.system("clear")

maca = 2.50
morango = 1.80
macas_compradas = float(input("Digite a quantidade em kilos de maçãs compradas:"))
morangos_compradas = float(input("Digite a quantidade em kilos de morangos comprados:"))

if macas_compradas and morangos_compradas < 15:
    preco_maca = 1.80
    preco_morango = 2.50
else:
    preco_maca = 1.50
    preco_morango = 2.20

valor_total = macas_compradas * preco_maca
valortotal = morangos_compradas * preco_morango

print()
print(f"Valor total da compra KG de maçãs: {valor_total:.2f}")
print(f"Valor total da compra KG de morangos: {valortotal:.2f}")