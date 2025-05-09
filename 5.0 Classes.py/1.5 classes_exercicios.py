import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Autor:
    nome: str
    biografia: str
   
@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

lista_livros = []
quantidade_livros = 2
for i in range(quantidade_livros):
    autor1 = Autor(
        nome = 0,
        biografia = input("Informe o nome do autor: ")
    )
    livro1 = Livro(
        titulo = input("Informe o título do livro: "),
        ano = int(input("Informe o ano que o livro foi públicado: ")),
        autor = Autor
    )
    autor2 = Autor(
        nome = 0,
        biografia = input("Informe o nome do autor: ")
    )
    livro2 = Livro(
        titulo = input("Informe o título do livro: "),
        ano = int(input("Informe o ano que o livro foi públicado: ")),
        autor = Autor
    )
    lista_livros.append(livro1)

for livro1, livro2 in lista_livros:
    print(f"Título: {livro1.titulo}")
print(f"Ano Públicado: {livro1.ano}")
print(f"Autor do Livro: {livro1.autor}")

print(f"Título: {livro2.titulo}")
print(f"Ano Públicado: {livro2.ano}")
print(f"Autor do Livro: {livro2.autor}")
