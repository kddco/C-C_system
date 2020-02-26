import hammer
from pynput.keyboard import Key, Listener


signal = 0
def start_on_press(key):
    print('{0} pressed'.format(
        key))
    global signal
    try:
        if key.char == 'v':
            signal = 1

        elif key == Key.shift:
            signal=0
            print("STOP")
        if signal == 1:
            print("GOsignal")
            hammer.active()

    except AttributeError:
        if key == Key.esc:
            # Stop listener
            return False


# def on_release(key):
#     print('{0} release'.format(
#         key))


with Listener(
        on_press=start_on_press
        #,on_release=on_release
) as listener:


    listener.join()