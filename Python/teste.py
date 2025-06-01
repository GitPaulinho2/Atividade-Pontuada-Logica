import os
import time
os.system("cls || clear")

produtos = []

#Tela de inicialização 

#--------------------------------------------------
print("\t\t== Iniciando o sistema de estoque ==")
time.sleep(1.5)
#--------------------------------------------------

#Função de adicionar produtos
def adicionar():
    nomeclatura = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço do produto: "))
    produto = {
        "nomeclatura": nomeclatura,
        "quantidade": quantidade,
        "preco": preco
    }
    produtos.append(produto)
    print("\n== Produto cadastrado com sucesso! ==\n")
    time.sleep(3.5)
    os.system("cls || clear")

#Função de Listar todos os produtos cadastrdos
def listar_produtos():
    if not produtos:
        print("\nNão a produto cadastrado.\nespere 2 segundos")
        time.sleep(2)
        return
    print("\nLista de produtos em estoque:")
    for produto in produtos:
        print(f"Produto: {produto['nomeclatura']} | Quantidade: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")
        
    print()
    time.sleep(6)
#Função que busca um produto pelo nome, ou por 1 letra
def buscar_produto():
    busca = input("Digite o nome do produto a buscar (letra, ou pelo nome): ")
    encontrados = [p for p in produtos if busca.lower() in p['nomeclatura'].lower()]
    if encontrados:
        print("Produtos encontrados:")
        for produto in encontrados:
            print(f"Produto: {produto['nomeclatura']} | Quantidade: {produto['quantidade']} | Preço: R${produto['preco']:.2f}")
            time.sleep(6)
    else:
        print("\nNenhum produto encontrado com esse nome.\nEspere 2 segundos")
        time.sleep(2)
    print()
#Função de atualizar um produto
def atualizar():
    nome = input("Digite o nome do produto para atualizar o estoque: ")
    for produto in produtos:
        if produto['nomeclatura'].lower() == nome.lower():
            print(f"Quantidade atual de '{produto['nomeclatura']}': {produto['quantidade']}")
            operacao = input("\nDigite '+' para adicionar ou '-' para remover do estoque: ")
            valor = int(input("\nDigite a quantidade: "))
            if operacao == '+':
                produto['quantidade'] += valor
                print(f"\nAdicionado {valor} unidades ao estoque de '{produto['nomeclatura']}'.")
            elif operacao == '-':
                if valor > produto['quantidade']:
                    print("\nErro: Não há unidades suficientes para remover.\nEspere 2 segundos")
                    time.sleep(2)

                else:
                    produto['quantidade'] -= valor
                    print(f"Removido {valor} unidades do estoque de '{produto['nome']}'.")
                    time.sleep(2)

            else:
                print("Operação inválida. \nEspere alguns segundos")
                time.sleep(2.5)
            print()
            return
    print("Produto não encontrado.\nEspere 2 segundos")
    time.sleep(2)



while True:
    os.system("cls || clear")
        #lista de opções
    print("=== Sistema de Estoque ===\n")
    print("1.\t Cadastrar produto")
    print("2.\t Listar todos os produtos")
    print("3.\t Buscar produto por nome")
    print("4.\t Atualizar estoque de produto")
    print("5.\t Sair\n")
    opcao = input("Escolha uma das opções acima: ")
    os.system("cls || clear")

#Caso o usuario digite uma das opções do sitema
    match opcao:
        case "1":
            adicionar()
        case "2":
            listar_produtos()
        case "3":
            buscar_produto()
        case "4":
            atualizar()
        case "5":
            print("Saindo do sistema. Até logo!")
            break
        #Caso o usuario digite uma opção de que não exista
        case _:
            print("Opção inválida.\nespere 3 segundos")
            time.sleep(3)
            os.system("cls || clear")