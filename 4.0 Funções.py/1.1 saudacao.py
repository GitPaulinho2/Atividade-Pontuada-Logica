import os
os.system("clear")

# Função sem retorno
# Definindo características da função.
def disciplina (nome):
    print(f"A disciplina {nome} faz parte do curso de DS.")

def saudacao (nome):
    print(f"Olá {nome}! Bem-vindo ao curso de DS!")

nome = input("Digite o seu nome: ")
nome_disciplina = input("Digite o nome da disciplina: ")

saudacao(nome) # Chamando a função.
disciplina(nome_disciplina) # Chamando a função.