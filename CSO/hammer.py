from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
print('初始化鍵盤滑鼠控制器')
keyboard = KeyboardController()
mouse = MouseController()


## 鍵盤控制
# 按下a键和释放a键
# Type a lower case A ;this will work even if no key on the physical keyboard is labelled 'A'
def active():
    keyboard.press('q')
    time.sleep(0.03)
    keyboard.release('q')
    ## 滑鼠控制
    mouse.press(Button.right)
    time.sleep(0.03)
    mouse.release(Button.right)
    time.sleep(0.06)
    keyboard.press('q')
    time.sleep(0.03)
    keyboard.release('q')



