import os
import time

os.system("clear")


print("Contagem regressiva.")
for i in range(100,122,2):
    print(f"Oi mundo: {i}")
    time.sleep(1) # espera 1 segundo

print("ACABOU.")
