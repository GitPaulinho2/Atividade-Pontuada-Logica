import os 

os.system("clear")

primeiro_numero = float(input("Digite seu primeiro número:"))
segundo_numero = float(input("Digite seu segundo número:"))
terceiro_numero = float(input("Digite seu terceiro número:"))

maior_numero = max (primeiro_numero, segundo_numero, terceiro_numero)
menor_numero = min (primeiro_numero, segundo_numero, terceiro_numero)

print(f"Maior número {maior_numero}")
print(f"Menor número {menor_numero}")

    