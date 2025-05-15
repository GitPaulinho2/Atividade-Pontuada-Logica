import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Info:
    nome: str
    data: str
    rg: str
    cpf: str

lista_pessoal = []
quantidade_usuario = 5

for i in range(quantidade_usuario):
    informacoes = Info(
    nome = input("Digite o nome do usuario: "),
    data = input("Digite a data de nascimento: "),
    rg = input("Digite o rg do usuario: "),
    cpf = input("Digite o cpf do usuario: ")
)
    lista_pessoal.append(informacoes)   
    os.system("clear")

nome_arquivo = "Funcionarios.txt"

with open (nome_arquivo, "a") as arquivo:
    for informacoes in lista_pessoal:
        arquivo.write(f"{informacoes.nome}, {informacoes.data}, {informacoes.rg}, {informacoes.cpf}\n")
print("\t=== Salvo com sucesso! ===\n")

print("\nAcessando dados em arquivos.")
try:
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")