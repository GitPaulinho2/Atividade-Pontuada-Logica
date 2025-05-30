import os
import time
os.system("clear")
from dataclasses import dataclass

@dataclass
class Calabreso:
    nome: str
    idade: str
    cpf: str
    ncartao: str

    def mostrar_dds(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cpf: {self.cpf}")
        print(f"Número Do Cartão: {self.ncartao}")

def verificar_nomes(nomes):
    if not nomes:
        print("A lista está vazia, rei🤑")
        return True
    return False

def Adicionar_calabreso(nomes):
    print("=| Informações Calabresais |=\n")
    calabreso = Calabreso(
    nome = input("Digite o seu nome: "),
    idade = input("Digite sua idade: "),
    cpf = input("Digite seu cpf: "),
    ncartao = input("Digite o número do cartão: ")
)
    nomes.append(calabreso)
def Atualizar_calabreso(nomes):
    if verificar_nomes(nomes):
        return
    print("!= Atualizando dados dos calabresos =!\n")
    dados_atualizar = input("Digite o cadastro que deseja atualizar: ")
    for calabreso in nomes:
        if calabreso.nome == dados_atualizar:
            os.system("clear")
            print("=== Atualize os novos dados do cliente == ")
            calabreso.nome = input("Digite o novo nome: ")
            calabreso.idade = input("Digite a nova idade: ")
            calabreso.cpf = input("Digite o novo cpf: ")
            calabreso.ncartao = input("Digite o novo número do cartão: ")
            print("=-= Dados do calabreso atualizados! =-=")
        return
    print(f"O funcionario com o nome ({dados_atualizar}) não foi encontrado!")
    os.system("clear")
def mostrar_calabresos(nomes):
   if verificar_nomes(nomes):
       return
   print("| Informações dos Calabresos |")
   for calabreso in nomes:
    calabreso.mostrar_dds()

def Explodir(nomes):
    os.system("clear")
    print("Inicando explosão")
    for i in range(5, 0, -1):
        print(f"Explosão em {i}")
        time.sleep(1.5)
    for i in range(2):
        os.system("clear")
        print("Nome Completo: Douglas Bilau")
        print("Idade: 69 anos")
        print("Horário que não tem ninguém em casa: 18:23")
        print("Cpf: 957.429.543-84")
        print("IP: 45.643.321.64")
        print("Endereço: Senzala mista")
    return

def vaic(nomes):
    os.system("clear")
    for i in range(0, 1001):
        print(f"VAAAAAAAI CORINTHIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAS\t{i}")
        time.sleep(0.1)

nomes = []

while True:
   os.system("clear")
   print("=-= Tabela de Calabresos 2025 =-=")
   print("1- Adicionar Calabreso")
   print("2- Atualizar Calabreso")
   print("3- Mostrar Calabresos")
   print("4- Explodir")
   print("5- Sair\n")

   opcao = int(input("Digite uma opção: "))

   match opcao:
        case 1:
            os.system("clear")
            Adicionar_calabreso(nomes)
            input("\nPressione Enter para continuar...\n")
        case 2:
            os.system("clear")
            Atualizar_calabreso(nomes)
            input("\nPressione Enter para continuar...\n")
            os.system("clear")
        case 3:
            os.system("clear")
            mostrar_calabresos(nomes)
            input("\nPressione Enter para continuar...\n")
        case 4:
            Explodir(nomes)
            input("\nPressione Enter para continuar...\n")
        case 8:
            vaic(nomes)
        case 5: 
            os.system("clear")
            print("Saindo...")
            time.sleep(3)
            break
        case _:
            print("Opção Inválida. \nTente novamente")