import pyautogui
import time

print("Pressione Ctrl + C para parar...\n")

while True:
    x, y = pyautogui.position()
    print(f"Coordenadas: X={x}  Y={y}")
    time.sleep(0.5)  # meio segundo de intervalo
