import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

lista_clientes = [] # Criando uma lista para adicionar clientes.
quantidade_clientes = 2 # Constante que define a quantidade de clientes.

# Laço de repetição para adicionar clientes.
print("Informe os dados do cliente ")
for i in range(quantidade_clientes):
    cliente = Cliente( # Instanciando um objeto.
        nome = input("Nome: "), # Não esqueça da vírgula.
        email = input("E-mail: "),
        telefone = input("Telefone: ") # No último não tem vírgula.
    )
    lista_clientes.append(cliente) # Adicionando um cliente na lista.
    
#  Laço de repetição para exibir os dados dos clientes.
print("\n= Exibindo dados dos clientes = ")
for cliente in lista_clientes:   # Mostra os dados por elementos na lista.
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")
