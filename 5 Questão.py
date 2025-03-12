import os

os.system("clear")

primeiro_numero = int(input("Digite o seu primeiro número:"))
operacao = input("Digite a sua operação:")
segundo_numero = int(input("Digite o seu segundo número:"))


match operacao:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        print("Opção inválida.")

print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Operação: {operacao}")
print(f"Resultado: {resultado}")
