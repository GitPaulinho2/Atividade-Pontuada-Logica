import os

os.system("cls || clear")

valor_gorjeta = 0
preco_total = 0
pratos_solicitados = ""

while True:
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
          """)
   
    opcao = int(input("Digite o número da opção desejada: "))
   
    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case _:
            print("Opção inválida. \nTente novamente... \n")
            prato = ""
            preco = 0
   
    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
   
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == "n":
        break
   
if preco_total > 0:
    gorjeta_garcom = input("Deseja pagar 10% do valor da sua nota como gorjeta para o garçom? ").lower()
    if gorjeta_garcom == "s":
        valor_gorjeta = preco_total * 0.10

total_pagar = preco_total + valor_gorjeta

print("\n=== Nota Fiscal ===")
print(f"Pratos solicitados: {pratos_solicitados}")
print(f"Valor da gorjeta: R$ {valor_gorjeta}")
print(f"Valor total da compra: R$ {total_pagar}")