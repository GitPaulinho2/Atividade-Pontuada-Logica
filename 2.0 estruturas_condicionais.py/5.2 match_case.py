import os

from sympy import resultant

os.system("clear") # Limpa o terminal.

primeiro_numero = int(input("Digite a primeira numero: "))
operacao = input("Digite a operação desejada:")
segundo_numero = int(input("Digite a segundo numero: "))



match operacao:
    case "/":
        resultado = primeiro_numero / segundo_numero
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case _:
        print("Opção inválida.")

print()
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Operação: {operacao}")
print(f"Resultado: {resultado}")
