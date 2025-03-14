import os
import time

os.system("clear")


print("Contagem regressiva.")
for i in range(1,22,2):
    print(f"Oi mundo: {i}")
    time.sleep(0.1) # espera 1 segundo

print("ACABOU!")
