import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

lista_clientes = [] 
quantidade_clientes = 2 


print("Informe os dados do cliente ")
for i in range(quantidade_clientes):
    cliente = Cliente( 
        nome = input("Nome: "), 
        email = input("E-mail: "),
        telefone = input("Telefone: ") 
    )
    lista_clientes.append(cliente) 
    
print("\n= Exibindo dados dos clientes = ")
for cliente in lista_clientes:   
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")

print("= Salvando os dados dos clientes = ")
nome_arquivo = "dados_clientes.txt"

# w -> escrita/salvar/sobrescerever
# a -> escrita/salvar/acumular
with open (nome_arquivo, "a") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome}, {cliente.email}, {cliente.telefone}\n")
print("\nSalvo com sucesso!")
