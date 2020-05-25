import pyautogui as pg
import time

with open('sample.cpp', 'r') as f:
    file_content = f.read()

print('Your script will run in 3 sec')

time.sleep(3)
pg.hotkey('winleft')
time.sleep(3)

pg.typewrite('vscode\n', 0.1)
time.sleep(4)

# optional
pg.hotkey('ctrl', 'shift', 'n')
time.sleep(4)

pg.hotkey('ctrl', 'n')
time.sleep(2)
pg.hotkey('winleft', 'up')
time.sleep(2)

pg.hotkey('ctrl', 's')
time.sleep(2)

pg.typewrite('abcd.txt\n', 0.2)

time.sleep(4)
pg.typewrite(file_content, 0.01)

