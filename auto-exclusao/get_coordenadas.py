import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()  # Obtém as coordenadas X e Y do mouse
        print(f'X: {x}, Y: {y}', end='\r')  # Imprime as coordenadas no console
        time.sleep(0.1)  # Atraso de 0,1 segundo para evitar sobrecarga de CPU
except KeyboardInterrupt:
    print("\nPrograma encerrado.")                           
