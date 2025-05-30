import os

os.system("clear")

print("""

============== Informações =============
1\tMasculino (M)
2\tFeminino (F)               
""")


nome = input("Digite o seu nome:")
sexo = input("Digite o seu sexo:")
estadocivil = input("Digite o seu estado civil:")

match sexo:
    case "M":
       print()
       print(f"Nome: {nome}")
       print(f"Sexo: {sexo}")
       print(f"Estado Civil: {estadocivil}")

    case "F":
        
        casada = int(input("Informe quantos anos esta casada:"))
        print()
        print(f"Nome: {nome}")
        print(f"Sexo: {sexo}")
        print(f"Estado Civil: {estadocivil}")
        print(f"Anos Casada: {casada}")
    case _:
        print("Opção Inválida")    