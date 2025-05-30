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


def salvar_funcionarios(lista):
    arquivo_funcionario = "dados_funcionarios.csv"

    with open (arquivo_funcionario, "a") as arquivo_do_funcionario:
        for funcionario in lista:
            arquivo_do_funcionario.write(f"{funcionario.nome}, {funcionario.data_adm}, {funcionario.matricula}, {funcionario.endereco}")

    print("Dados dos funcionarios salvos com exito.")
def salvar_clientes(lista):
    arquivo_cliente = "dados_clientes.csv"
    
    with open (arquivo_cliente, "a") as arquivo_do_cliente:
        for cliente in lista:
            arquivo_do_cliente.write(f"{cliente.nome}, {cliente.data}, {cliente.endereco}")
    print("Dados dos clientes salvos com exito.")

lista_funcionario = []
lista_cliente = []

for i in range(1):
    print("Digite os dados do Funcionario: ")
    funcionarios = Funcionario(
    nome = input("Digite o nome do usuario: "),
    data_adm = input("Digite a data de nascimento: "),
    matricula = input("Digite a matricula do usuario: "),
    endereco = input("Digite o endereço do usuario: ")
)
    lista_funcionario.append(funcionarios) 
    print("Digite os dados do Cliente:\n ")  
    clientes = Cliente(
        nome = input("Digite o seu nome: "),
        data = input("Digite a sua data de nascimento: "),
        endereco = input("Digite o seu endereço: ")        
    )
    lista_cliente.append(clientes)   
    os.system("clear")

salvar_funcionarios(lista_funcionario)
salvar_clientes(lista_cliente)