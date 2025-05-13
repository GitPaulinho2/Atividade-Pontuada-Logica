import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Funcionario:
    nome: str
    data_adm: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    data: str
    endereco: str

lista_funcionario = []
lista_cliente = []
quantidade_usuario = 3

for i in range(quantidade_usuario):
    funcionarios = Funcionario(
    nome = input("Digite o nome do usuario: "),
    data_adm = input("Digite a data de nascimento: "),
    matricula = input("Digite o rg do usuario: "),
    endereco = input("Digite o cpf do usuario: ")
)
    clientes = Cliente(
        nome = input("Digite o seu nome: "),
        data = input("Digite a sua data de nascimento: "),
        endereco = input("Digite o seu endereço: ")        
    )
    lista_funcionario.append(funcionarios)   
    lista_cliente.append(clientes)   
    os.system("clear")

nome_arquivo = "Funcionarios.txt"

with open (nome_arquivo, "a") as arquivo:
    for funcionarios in lista_funcionario:
        arquivo.write(f"{funcionarios.nome}, {funcionarios.data_adm}, {funcionarios.matricula}, {funcionarios.endereco}\n")

print("\n== Funcionarios ==")
try:
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

arquivo_cliente = "Clientes.txt"

with open (arquivo_cliente, "a") as cliente:
    for clientes in lista_cliente:
        cliente.write(f"{clientes.nome}, {clientes.data}, {clientes.endereco}\n")
print("=== Clientes ===")

try:
    with open (arquivo_cliente, "r") as cliente:
        for linha in linhas:
            linhas = cliente.readlines()
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("\nAcessando dados")