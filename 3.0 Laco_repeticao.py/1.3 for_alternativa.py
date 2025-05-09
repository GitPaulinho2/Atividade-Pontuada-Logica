import os
import time

os.system("clear")


print("Contagem regressiva.")
for i in range(100, 121):
    if i % 2 == 0:
        print(f"Número: {i}")
        time.sleep(1)

