import os 
from dataclasses import dataclass
os.system("clear")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    # Variáveis = Atributos
    nome: str
    idade: int
    endereco: Endereco
    
    # Função = Método
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}, número: {self.endereco.numero}\n")
endereco1 = Endereco ("Rua B", 25)
pessoa1 = Pessoa("Marta", 28, endereco1)
pessoa1.exibir_dados()




