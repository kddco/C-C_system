import hammer
from pynput.keyboard import Key, Listener


signal = 0
def start_on_press(key):
    print('{0} pressed'.format(
        key))
    try:
        if key.char == 'v':
            with Listener(
                    on_press = stop_on_press
            ) as listener:
                listener.join()
            return False

    except AttributeError:
        if key == Key.esc:
            # Stop listener
            print("esc")
            return False

def stop_on_press(key):
    print("動作停止偵測開始")
    if key == Key.shift:
        print("動作停止")
        return False

# def on_release(key):
#     print('{0} release'.format(
#         key))


with Listener(
        on_press=start_on_press
        #,on_release=on_release
) as listener:
    listener.join()