import os
import time
os.system("clear")

contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 9999
mulheres5k = 0
while True:

    print("""
Código\tDescrição
        
1\tAdicionar pessoa
2\tExibir resultados
3\tSair
 """)

    codigo = int(input("Digite uma das 3 opções:"))

    match codigo:
        case 1:
            sexo = input("Informe seu sexo com 'M' ou 'F':")
            salario = float(input("Informe seu sálario:"))
            idade = int(input("Informe sua idade:"))
            contador += 1
            soma_salario += salario
        
            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade
            if sexo == "F" and salario >= 5000:
                mulheres5k += 1

            os.system("clear")
        case 2:
            if contador > 0:
                media_salario_grupo = soma_salario / contador
                print("\n = Exibindo resultados = ")          
                print(f"Média de salario do grupo: {media_salario_grupo} ")          
                print(f"Maior idade do grupo: {maior_idade} ")          
                print(f"Menor idade do grupo: {menor_idade} ")          
                print(f"Quantidade de mulheres com sálario a partir de 5 mil: {mulheres5k}")          
            else:
                print("Não existem dados para exibir.")
            time.sleep(3)
            os.system("clear")
        case 3:
           print("\nFim do programa.")
           break
        case _:
            print("\nOpção Inválida.")
            time.sleep(3)
            os.system("clear")