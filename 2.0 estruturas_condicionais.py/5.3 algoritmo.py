import os 

os.system("clear")


print("""
================== MENU ===================

Código    \tPrato   \t\tValor
1 \t\tPicanha     \t\t R$25.00
2 \t\tLasanha     \t\t R$20.00
3 \t\tStrogonoff     \t\t R$18.00
4 \t\tBife Acebolado\t\t R$15.00
5 \t\tPão com ovo   \t\t R$5.00
""")

opcao = int(input("Digite a opção desejada: "))

match opcao:
    case 1:
      prato = "Picanha"
      valor = 25
    case 2:
      prato = "Lasanha"
      valor = 20
    case 3:
      prato = "Strogonoff"
      valor = 18
    case 4:
      prato = "Bife Acebolado"
      valor = 15
    case 5:
     prato = "Pão Com Ovo"
     valor = 5
    case _:
     prato = "Opção invalida"
     valor = 0

print()
print(f"Prato:{prato}")
print(f"Valor: R$ {valor:.2f}")

