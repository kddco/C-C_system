from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
print('初始化鍵盤滑鼠控制器')
keyboard = KeyboardController()
time.sleep(5)
while True:
    keyboard.press('q')
    time.sleep(0.03)
    keyboard.release('q')



