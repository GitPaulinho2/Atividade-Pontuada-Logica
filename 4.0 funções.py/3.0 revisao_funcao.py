import os 
os.system("clear")

lista_notas = [] # Criando uma lista.
QUANTIDADE_NOTAS = 2 # criando uma constante.

# Função para calcular média.
def calcular_media(lista):
    # sum(lista) irá somar os valores na lista
    # len(lista) irá mostrar a quantidade de valores na lista.
    media = sum(lista) / len(lista)
    return media
    # Solicitando dados apra o usuário.
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    lista_notas.append(nota)

# Chamando a função para calcular a média.
# Enviando a lista de notas como parâmetro.
# Inserindo na variável 'media' o cálculo retornado pela função.
media = calcular_media(lista_notas)

# Exibindo a média.
print(f"\nMédia: {media}")