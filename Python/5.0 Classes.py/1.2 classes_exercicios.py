import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Pessoa:
    # Variáveis = Atributos
    nome: str
    idade: int
    numero: int
    cidade: str
    logradouro: str
    endereco: str
    
    # Função = Método
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}, número: {self.endereco.numero}\n")


pessoa1 = Pessoa(
nome = input("Digite o seu nome:"))
idade = int(input("Digite a sua idade:"))
logradouro = int(input("Digite seu logradouro: "))
endereco = input("Digite o seu endereço: ")
numero = int(input("Digite o seu número: "))
cidade = input("Digite sua cidade: ")
pessoa1.exibir_dados()




