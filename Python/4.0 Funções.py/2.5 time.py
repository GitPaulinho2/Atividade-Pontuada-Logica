import os
from datetime import datetime
os.system("clear")


# def calcular_idade (ano_nascimento):
    #return 2025 - ano_nascimento

def calcular_idade(ano_nascimento):
    return datetime.now().year - ano_nascimento

ano_nascimento = int(input("Digite o seu ano de nascimento: "))

idade = calcular_idade(ano_nascimento)

print(f"Idade: {idade}")