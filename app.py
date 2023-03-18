#link to access available keyboard functions https://pyautogui.readthedocs.io/en/latest/quickstart.html

import pyautogui #import library
import time

pyautogui.alert('O código será acionado quando você precionar OK. Pós isso não interrompa o código clicando em algo do teclado ou do mouse.')

pyautogui.PAUSE = 0.5 #we set a break between each task

pyautogui.press('winleft') #command that presses a keyboard key (open windows)

pyautogui.write('chome') #allows you to write a text

pyautogui.press('enter')

time.sleep(1) #give a time of 1 second

pyautogui.write('https://drive.google.com/drive/my-drive')

pyautogui.press('enter')

pyautogui.hotkey('win', 'd') #click two or more keys

pyautogui.moveTo(1849, 50) #positions the mouse to the desired position of the x and y axes

pyautogui.mouseDown() #press the left mouse button

pyautogui.moveTo(980, 600)

pyautogui.hotkey('alt', 'tab')
time.sleep(1) #wait 1 second for the browser to open

pyautogui.mouseUp() #release the mouse button

time.sleep(5) #wait 5 seconds to upload

pyautogui.alert('O código foi finalizado com sucesso! Pode usar seu computador normalmente.')
