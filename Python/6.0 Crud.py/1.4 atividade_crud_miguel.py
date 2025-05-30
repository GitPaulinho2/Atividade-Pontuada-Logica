import os
from dataclasses import dataclass
import time
#importar o csv
import csv
os.system("cls || clear")
#logo linda e maravilhasa
print("== Bem vindo ao Dendê tech ==")

lista_funcionarios = [] #lista
@dataclass
class Funcionario:
    nome: str
    cpf: str
    data_nascimento: str
    funcao: float
    #mostar os dados
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Cargo: {self.data_nascimento}")
        print(f"Sálario: {self.funcao}\n")
#analizar se a lista estar vazia
def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False
#case 1 (adicionar)
def adicionar(lista):
    print("= Digite os dados do funcionário = ")
    funcionario = Funcionario(
        nome=input("Nome: "),
        cpf=input("CPF: "),
        data_nascimento=input("Cargo: "),
        funcao=input("Sálario: ")
    )
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso.\n")
#case 2 (mostrar)
def mostrar_funcionarios(lista):
    if verificar_lista_vazia(lista):
        return
    print("\n= Lista de funcionários =")
    for funcionario in lista:
        funcionario.mostrar_dados()
#case 3 (atualizar)
def atualizar(lista):
    if verificar_lista_vazia(lista):
        return
    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
    for funcionario in lista:
        if funcionario.nome == nome_atualizar:
            print("= Digite os novos dados do funcionário = ")
            funcionario.nome = input("Nome: ")
            funcionario.cpf = input("CPF: ")
            funcionario.data_nascimento = input("Cargo: ")
            funcionario.funcao = input("Sálario: ")
            print("Funcionário atualizado com sucesso.\n")
            return
    print(f"\nO funcionário com o nome '{nome_atualizar}' não foi encontrado.\n")
#case 5 (exporta informações para o csv)  
def exportar_csv(lista, nome_arquivo="Funcionarios.csv"):
    if verificar_lista_vazia(lista):
        return
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Nome", "CPF", "Cargo", "Sálario"])
        for funcionario in lista:
            writer.writerow([funcionario.nome, funcionario.cpf, funcionario.data_nascimento, funcionario.funcao])
    print(f"\nDados exportados com sucesso para '{nome_arquivo}'.\n")
#case 4 (excluir um funcionario da existencia)
def excluir(lista):
    if verificar_lista_vazia(lista):
        return
    nome_excluir = input("Digite o nome do funcionário que deseja excluir: ")
    for funcionario in lista:
        if funcionario.nome == nome_excluir:
            lista.remove(funcionario)
            print("Funcionário excluído com sucesso.\n")
            return
    print("Funcionário não encontrado.\n")

#codigo principal
def main():
 
    while True:
        os.system("cls || clear")
        print("== Escolha uma opção abaixo ==\n")
        print("1 - Adicionar funcionário")
        print("2 - Mostrar funcionários")
        print("3 - Atualizar funcionário")
        print("4 - Excluir funcionário")
        print("5 - Exportar para CSV")
        print("6 - Sair\n")
        opcao = input("Escolha uma opção: ") 

        #match e seus cases
        match opcao:
            case "1":
                os.system("cls || clear")
                adicionar(lista_funcionarios)
                input("Pressione Enter para continuar...")
            case "2":
                os.system("cls || clear")
                mostrar_funcionarios(lista_funcionarios)
                input("Pressione Enter para continuar...")
            case "3":
                os.system("cls || clear")
                atualizar(lista_funcionarios)
                input("Pressione Enter para continuar...")
            case "4":
                os.system("cls || clear")
                excluir(lista_funcionarios)
                input("Pressione Enter para continuar...")
            case "5":
                os.system("cls || clear")
                exportar_csv(lista_funcionarios)
                input("Pressione Enter para continuar...")
            case "6":
                print("Saindo do programa. Até logo!")
                break
            case _:
                #opção invalida
                print("Opção inválida.")
                input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()