import os 

os.system("clear")


print("""
=//////////// Caléndario \\\\\\\\\\\\\\\\\\\\\\\=
Código  \tDia Da Semana
1  \t\tDomingo
2  \t\tSegunda-Feira
3  \t\tTerça-Feira
4  \t\tQuarta-Feira
5  \t\tQuinta-Feira
6  \t\tSexta-Feira
7  \t\tSábado
""")
      
dia = input("Digite um número para o dia da semana:")   

match dia:
    case "1":
        print("Domingo")
        print("Final De Semana")
    case "2":
        print("Segunda-Feira")
        print("Dia útil")        
    case "3":
        print("Terça-Feira")
        print("Dia útil")        
    case "4":
        print("Quarta-Feira")
        print("Dia útil")        
    case "5":
        print("Quinta-Feira")
        print("Dia útil")        
    case "6":
        print("Sexta-Feira")
        print("Dia útil")        
    case "7":
        print("Sábado")
        print("Final De Semana")
    case _:
        print("Inválido")       

