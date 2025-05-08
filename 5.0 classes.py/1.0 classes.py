import os 
from dataclasses import dataclass
os.system("clear")


# Criando uma classe
@dataclass
class Pessoa:
    nome: str
    idade: int

# Aplicando características da classe.
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

print(f"Nome: {pessoa1.nome} tem {pessoa1.idade} anos.")
print(f"Nome: {pessoa2.nome} tem {pessoa2.idade} anos.")

