import os

os.system("clear")

primeiro_numero = int(input("Digite o primeiro número:"))
segundo_numero = int(input("Digite o segundo número:"))
soma = (primeiro_numero + segundo_numero)
media = (primeiro_numero * segundo_numero)

if primeiro_numero == segundo_numero:
    print(f"Valores iguais: {soma}")
else:
    print(f"Valores diferentes: {media}")