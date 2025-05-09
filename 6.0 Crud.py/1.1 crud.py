import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Carro:
    marca: str
    modelo: str
    categoria: str
    preco: int

lista_carro = []
quantidade_carro = 2

for i in range(quantidade_carro):
    carro = Carro(
    marca = input("Digite a marca do carro: "),
    modelo = input("Digite o modelo do carro: "),
    categoria = input("Digite a categoria do carro: "),
    preco = int(input("Digite o preço do carro: "))
)
    lista_carro.append(carro)   
    os.system("clear")
print("\n= Exibindo dados dos carros = ")
for carro in lista_carro:   
    print(f"Marca do carro: {carro.marca}")
    print(f"Modelo do carro: {carro.modelo}")
    print(f"Categoria: {carro.categoria}")
    print(f"Preço do carro: {carro.preco}")
    
    
nome_arquivo = "carros.txt"

with open (nome_arquivo, "a") as arquivo:
    for carro in lista_carro:
        arquivo.write(f"{carro.marca}, {carro.modelo}, {carro.categoria}, {carro.preco}\n")
print("\nSalvo com sucesso!")
