import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    cpf: str
    data_nascimento: str
    funcao: str
   
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"Função: {self.funcao}")
        print()
       
   
def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar(lista):
    print("= Digite os dados do funcionário = ")
    funcionario = Funcionario(
        nome=input("Nome: "),
        cpf=input("CPF: "),
        data_nascimento=input("Data de nascimento: "),
        funcao=input("Função: ")
    )
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso.")
   
def mostrar_funcionarios(lista):
    if verificar_lista_vazia(lista):
        return
   
    print("\n= Lista de funcionários =")
    for funcionario in lista:
        funcionario.mostrar_dados()
       
def atualizar(lista):
    if verificar_lista_vazia(lista):
        return
   
    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
    encontrado = False
   
    for funcionario in lista:
        if funcionario.nome == nome_atualizar:
            print("= Digite os dados do funcionário = ")
            funcionario.nome=input("Nome: "),
            funcionario.cpf=input("CPF: "),
            funcionario.data_nascimento=input("Data de nascimento: "),
            funcionario.funcao=input("Função: ")
            encontrado = True
            break
   
    if not encontrado:
        print(f"\nO funcionário com o nome {funcionario.nome} não foi encontrado.")
       
    mostrar_funcionarios(lista)
   
def excluir(lista):
    if verificar_lista_vazia(lista):
        return
   
    nome_excluir = input("Digite o nome do funcionário: ")
    for funcinario in lista_funcionarios:
        if funcinario.nome == nome_excluir:
            lista_funcionarios.remove(nome_excluir)
            print("Funcionário excluído com sucesso.")
        else:
            print("Funcionário não encontrado.")
   

lista_funcionarios = []
for i in range(1):
    adicionar(lista_funcionarios)  
   
mostrar_funcionarios(lista_funcionarios)

atualizar(lista_funcionarios)

excluir(lista_funcionarios)