import pyautogui

pyautogui.alert('O código será acionado quando você precionar OK. Pós isso não interrompa o código clicando em algo do teclado ou do mouse.')

pyautogui.hotkey('win', 'd')
pyautogui.hotkey('alt', 'f4')
pyautogui.press('enter')