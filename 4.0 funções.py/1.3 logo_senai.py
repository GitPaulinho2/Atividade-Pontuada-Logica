import os
os.system("clear")

# Função sem retorno
# Definindo características da função.
def logo_senai():
    os.system("clear")
    print("=== SENAI ===")
    print("Aulas de lógica")

logo_senai() # Chamando a função.
nome = input("Digite seu nome:")
logo_senai() # Chamando a função.
idade = input("Digite sua idade:")
logo_senai() # Chamando a função.
print(f"Nome: {nome}")
print(f"Idade: {idade}")
