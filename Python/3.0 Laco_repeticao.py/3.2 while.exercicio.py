import os
import time
os.system("clear")

contador = 0
soma_salario = 0
maior_salario = 0
menor_salario = 9999
total_familias = 0
soma_filhos = 0
while True:
    print("""
Código\tDescrição
        
1\tAdicionar Familia
2\tSair e exibir resultados
 """)

    codigo = int(input("Digite uma das 3 opções:"))

    match codigo:
        case 1:
            salario = int(input("Informe o seu sálario: "))
            numero_filhos = int(input("Informe o número de filhos: "))
            total_familias += 1
            contador += 1
            soma_salario += salario
            soma_filhos += numero_filhos
        
            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario
            
            os.system("clear")
        case 2:
            if contador > 0:
                media_salario_populacao = soma_salario / contador
                media_fihos = soma_filhos / contador
                print("\n = Exibindo resultados = ")          
                print(f"Média de salario do grupo: {media_salario_populacao} ")          
                print(f"Total de familais cadastradas: {total_familias} ")                  
                print(f"Média de filhos: {numero_filhos} ")                  
                print(f"Maior salario do grupo: {maior_salario} ")          
                print(f"Menor salario do grupo: {menor_salario} ")                  
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