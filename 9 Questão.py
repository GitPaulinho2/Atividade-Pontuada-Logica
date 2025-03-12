import os

os.system("clear")
renda_mensal = float(input("Informe sua renda mensal: R$ "))
valor_emprestimo = float(input("Informe o valor do empréstimo desejado: R$ "))
numero_prestacoes = int(input("Informe o número de prestações desejadas: "))

def analisar_emprestimo(renda_mensal, valor_emprestimo, numero_prestacoes):

    maxemprestimo = renda_mensal * 10
    
    maxprestacao = renda_mensal * 0.3
    
    valor_prestacao = valor_emprestimo / numero_prestacoes

    if valor_emprestimo <= maxemprestimo and valor_prestacao <= maxprestacao:
        return "Empréstimo concedido."
    else:
        return "Empréstimo negado."


resultado = analisar_emprestimo(renda_mensal, valor_emprestimo, numero_prestacoes)
print(resultado)