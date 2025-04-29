import os
os.system("clear")
dias_semana = {
    1: "Segunda-Feira",
    2: "Terça-Feira",
    3: "Quarta-Feira",
    4: "Quinta-Feira",
    5: "Sexta-Feira",
    6: "Sábado",
    7: "Domingo"
}

aulas_semana = {
    1: "Projeto de vida, Biologia, Filosofia, História Afro, Historia Afro",
    2: "Português, Português, ",
    3: "Geografia, Física, Matemática, Matemática",
    4: "Física, Sociologia, Redação",
    5: "Inglês, Matemática, História",
    6: "Não há aulas hoje",
    7: "Não há aulas hoje"
}

while True:
    print("""
Código   ||   Dia
      
1\tSegunda-Feira      
2\tTerça-Feira
3\tQuarta-Feira
4\tQuinta-Feira
5\tSexta-Feira   
""")
    opcao = int(input("Digite o dia da semana: "))

    #Esse código ainda não está 100% bom, essa parte por exemplo se você apertar qualquer botão vai repetir a pergunta.
    mais_pedidos = input("\nDeseja ver outro dia da semana?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == "n":
        break

if opcao in dias_semana:
    dia_escolhido = dias_semana


    print("=== Resultado ===")
    print(f"Dia Selecionado: {dia_escolhido[opcao]}")
    print(f"Aulas do Dia: {aulas_semana[opcao]}")

    #atualizando a tabela quando ter mais aulas :emoji insano: