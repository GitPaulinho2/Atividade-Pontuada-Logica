import os
import time
from dataclasses import dataclass
os.system("clear")

@dataclass
class Funcionario:
    nome: str
    data_nasc: str
    cpf: str
    funcao: str


def verificar_lista_funcionario(lista_funcionario):
    if not lista_funcionario:
        print("A lista está vazia")
        return True

    return False

def adicionar (lista_funcionario):
    nome = input("Digite o nome do funcionário: ")
    data_nasc = input("Digite a data de nascimento: ")
    cpf = input("Digite o seu cpf: ")
    funcao = input("Digite a sua função: ")
    lista_funcionario.append(nome)
    lista_funcionario.append(data_nasc)
    lista_funcionario.append(cpf)
    lista_funcionario.append(funcao)
    print(f"{nome} virou clt")

def mostrar (lista_funcionario):
    if verificar_lista_funcionario(lista_funcionario):
        return
    
    print("= Lista de nomes =")
    for nome in lista_funcionario:
        print(f"- {nome}")

def atualizar(lista_funcionario):
    if verificar_lista_funcionario(lista_funcionario):
        return
    
    mostrar(lista_funcionario)
    nome_antigo = input("Digite o nome que deseja mudar: ") 
    if nome_antigo in lista_funcionario:
        novo_nome = input(f"Digite o novo nome: ")
        indice = lista_funcionario.index(nome_antigo)
        lista_funcionario[indice] = novo_nome
        print(f"{nome_antigo} foi mudado para {novo_nome}!")
    else:
        print(f"O nome {nome_antigo} não encontrado!")

nomes = []

while True:
    print("1- Adicionar Funcionario")
    print("2- Atualizar Funcionario")
    print("3- Mostrar Funcionario")
    print("4- Sair")
    opcao = int(input("Digite uma opção: "))

    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            atualizar(nomes)
        case 3:
            mostrar(nomes)
        case 4:
            print("Saindo do programa.")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")
    if opcao != 1:
        time.sleep(5)
    os.system("cls || clear")