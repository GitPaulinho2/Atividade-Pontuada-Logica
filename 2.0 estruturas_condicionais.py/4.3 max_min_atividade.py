import os

os.system("clear") # Limpa o terminal.

#Utilizando condicionais aninhados.
primeiro_numero = float(input("Digite a primeira numero: "))
segundo_numero = float(input("Digite a segundo numero: "))


media = (primeiro_numero / segundo_numero) / 2
soma  = (primeiro_numero + segundo_numero)
produto = (primeiro_numero * segundo_numero)
igual = (primeiro_numero == segundo_numero)

maior_numero = max (primeiro_numero, segundo_numero)
menor_numero = min (primeiro_numero, segundo_numero)


print(f"Média {media}")
print (f"Soma {soma}")
print(f"Produto {produto}")
print(f"Menor Número {segundo_numero}")
print(f"Maior Número {primeiro_numero}")

if maior_numero == menor_numero:
    print("Os números são iguais")

else:
    print("Os números não são iguais")