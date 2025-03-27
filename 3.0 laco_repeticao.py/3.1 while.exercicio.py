import os
os.system("clear")

sexo = int(input("Informe seu sexo:"))
salario = int(input("Informe seu sálario:"))
idade = int(input("Informe sua idade:"))

while True:
    print("""
Código\tDescrição
      
1\tAdicionar pessoa
2\tExibir resultados
3\tSair
""")

    codigo = int(input("Digite uma das 3 opções:"))

    match codigo:
        case "1":
            sexo = int(input("Informe seu sexo:"))
            salario = int(input("Informe seu sálario:"))
            idade = int(input("Informe sua idade:"))
        case "2":
            break
            

        
