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
    def exibir_detalhes(livro):
        print(f"Autor do Livro: {livro.autor.biografia}")
        print(f"Título: {livro.titulo}")
        print(f"Ano Públicado: {livro.ano}")
autor = Autor(
    nome = 0,
    biografia = input("Informe o nome do autor: ")
    )
livro = Livro(
    titulo = input("Informe o título do livro: "),
    ano = int(input("Informe o ano que o livro foi públicado: ")),
    autor = autor
    )
livro.exibir_detalhes()