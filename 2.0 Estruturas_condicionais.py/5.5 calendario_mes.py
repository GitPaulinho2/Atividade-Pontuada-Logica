import os 

os.system("clear")


print("""
=//////////// Caléndario \\\\\\\\\\\\\\\\\\\\\\\=
Código  \tDia Da Semana
1  \t\tJaneiro
2  \t\tFevereiro
3  \t\tMarço
4  \t\tAbril
5  \t\tMaio
6  \t\tJunho
7  \t\tJulho
8  \t\tAgosto
9  \t\tSetembro
10 \t\tOutubro
11 \t\tNovembro
12 \t\tDezembro
""")
      
dia = input("Digite um número para um mês do ano:")   

match dia:
    case "1":
        print("Janeiro")
    case "2":
        print("Fevereiro")    
    case "3":
        print("Março")       
    case "4":
        print("Abril")       
    case "5":
        print("Maio")       
    case "6":
        print("Junho")       
    case "7":
        print("Julho")
    case "8":
        print("Agosto")
    case "9":
        print("Setembro")
    case "10":
        print("Outubro")
    case "11":
        print("Novembro")
    case "12":
        print("Dezembro")
    case _:
        print("Inválido")       
