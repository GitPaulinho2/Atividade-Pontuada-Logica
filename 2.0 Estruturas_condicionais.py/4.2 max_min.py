import os

os.system("clear") # Limpa o terminal.

#Utilizando condicionais aninhados.
primeiro_numero = float(input("Digite a primeira numero: "))
segundo_numero = float(input("Digite a segundo numero: "))


media = (primeiro_numero / segundo_numero) / 2
soma  = (primeiro_numero + segundo_numero)
produto = (primeiro_numero * segundo_numero)


print(f"Média: {media}")
print (f"Soma: {soma}")
print(f"Produto {produto}")
print(f"Menor Número {primeiro_numero}")
print(f"Maior Número {segundo_numero}")



if primeiro_numero <  segundo_numero:
    maior_numero = segundo_numero
    menor_numero = primeiro_numero

else:
    maior_numero = primeiro_numero
    menor_numero = segundo_numero

