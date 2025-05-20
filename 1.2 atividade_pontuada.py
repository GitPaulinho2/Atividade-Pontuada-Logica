import os
import time
from dataclasses import dataclass
os.system("clear")

@dataclass
class Funcionario:
    nome: str
    cpf: str
    cargo: str
    salario: str

def verificar_lista_funcionario(lista_funcionario): # verificando lista
    if not lista_funcionario: # verificando se a lista está vazia 
        print("A lista está vazia") # ta vazia 👍
        return True

    return False

def adicionar (lista_funcionario): # adicionando novo funcionario
    nome = input("Digite o nome do funcionário: ") 
    cpf = input("Digite o cpf do funcionario: ")
    cargo = input("Digite o cargo do funcionario: ")
    salario = input("Digite o salário do funcionario: ")
    lista_funcionario.append(nome)
    lista_funcionario.append(cpf)
    lista_funcionario.append(cargo)
    lista_funcionario.append(salario)
    print(f"{nome} virou clt")

def atualizar(lista_funcionario): # mostrando a lista
    if verificar_lista_funcionario(lista_funcionario):
        return
    
    mostrar(lista_funcionario)
    nome_atualizar = input("Digite o nome que deseja mudar: ") 
    for funcionario in nomes:
        if funcionario.nome == nome_atualizar:
            print("= Digite os novos dados do funcionário = ")
            funcionario.nome = input("Nome: ")
            funcionario.cpf = input("CPF: ")
            funcionario.cargo = input("Cargo: ")
            funcionario.salario = input("Sálario: ")
            print("Funcionário atualizado com sucesso.\n")
            return
    print(f"\nO funcionário com o nome '{nome_atualizar}' não foi encontrado.\n")


def mostrar (lista_funcionario):
    if verificar_lista_funcionario(lista_funcionario):
        return
    
    print("= Lista de nomes =")
    for nome in lista_funcionario:
        print(f"- {nome}")

def excluir(lista_nomes):
    if verificar_lista_funcionario(lista_nomes):
        return
   
    mostrar(lista_nomes) # Mostrando lista de usuários.
   
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print(f"{nome_remover} foi excluído com sucesso.")
    else:
        print(f"O nome {nome_remover} não foi encontrado.")    

nomes = [] # Lista de nomes

while True:
    print("= Gerenciamento de Funcionarios =")
    print("1 - Adicionar")
    print("2 - Atualizar")
    print("3 - Listar nomes")
    print("4 - Excluir")
    print("5 - Sair")
    opcao = int(input("Digite uma das opções: "))

    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            atualizar(nomes)
        case 3:
            mostrar(nomes)
        case 4:
            excluir(nomes)
        case 5:
            print("Saindo")
            break
        case _:
            print("Opção Inválida, Tente novamente")
    if opcao != 1:
        time.sleep(5)
    os.system("clear")
