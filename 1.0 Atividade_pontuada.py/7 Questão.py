import os

os.system("clear")

nome_produto = input("Informe o produto comprado: ")
quantidade = int(input("Informe a quantidade adquirida: "))
valor_total = float(input("Digite o valor total gasto: R$"))

preco_unitario = valor_total / quantidade

total = valor_total

match quantidade:
    case _ if quantidade <= 5:
        desconto = total * 0.02
    case _ if quantidade <= 10:
        desconto = total * 0.03
    case _ if quantidade > 10:
        desconto = total * 0.05

totalapagar = total - desconto

print()
print(f"Produto: {nome_produto}")
print(f"Quantidade adquirida: {quantidade}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Total sem desconto: R${total:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total a pagar: R${totalapagar:.2f}")