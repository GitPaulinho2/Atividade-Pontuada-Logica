import os 
from dataclasses import dataclass
os.system("clear")

# Criando uma classe
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

# Aplicando características da classe.
pessoa1 = Pessoa(
    nome = input("Digite o nome da primeira pessoa: "),
    idade = int(input("Digite a sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura: ")),
    )
os.system("clear")
pessoa2 = Pessoa(
    nome = input("Digite o nome da segunda pessoa: "),
    idade = int(input("Digite a idade: ")),
    peso = float(input("Digite o peso: ")),
    altura = float(input("Digite a altura: ")),
    )
# Aplicando características da classe Pet


print("\n== Dados da Pessoa ==")

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade:.2f} Peso: {pessoa1.peso:.2f} Altura: {pessoa1.altura:.2f}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade:.2f} Peso: {pessoa2.peso:.2f} Altura: {pessoa2.altura:.2f}")


