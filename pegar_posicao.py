import time
import pyautogui

time.sleep(5)
print(pyautogui.position())

# Como scrollar - números positivos ele scrolla para cima e negativos para baixo
pyautogui.scroll(-200)