import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: int

lista_livro = []
quantidade_livro = 3

for i in range(quantidade_livro):
    livro = Livro(
    nome = input("Digite o nome do livro: "),
    autor = input("Digite o nome do autor: "),
    categoria = input("Digite a categoria do livro: "),
    preco = int(input("Digite o preço do livro: "))
)
    lista_livro.append(livro)   
    os.system("clear")

nome_arquivo = "Catálogo_livros.txt"

with open (nome_arquivo, "a") as arquivo:
    for livro in lista_livro:
        arquivo.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, {livro.preco}\n")
print("\t=== Salvo com sucesso! ===\n")

print("\nAcessando dados em arquivos.")
try:
    with open(nome_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")