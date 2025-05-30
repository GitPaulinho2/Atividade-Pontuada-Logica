import os

os.system("clear") # Limpa o terminal.

#Utilizando condicionais aninhados.

maçã = 1,30
maca_comprada = float(input("Informe a quantidade de maçãs desejadas:"))

if maca_comprada < 12:
    preco_maca = 1.30
else:
    preco_maca = 1.00

valor_total = maca_comprada * preco_maca

print()
print(f"Valor total da compra R$ {valor_total:.2f}")
