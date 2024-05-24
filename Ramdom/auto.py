import threading
import time
from pynput import keyboard

class KeyPresser:
    def __init__(self):
        self.is_active = False
        self.interval = 0.1  # Time interval in seconds
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.thread = threading.Thread(target=self.press_keys)
        self.thread.daemon = True

    def on_press(self, key):
        try:
            if key.char == 't':  # Toggle key (change 't' to any key you prefer)
                self.is_active = not self.is_active
                if self.is_active:
                    print("Macro started")
                else:
                    print("Macro stopped")
        except AttributeError:
            if key == keyboard.Key.esc:  # Exit key
                return False

    def press_keys(self):
        from pynput.keyboard import Controller
        controller = Controller()
        while True:
            if self.is_active:
                controller.press('f')
                controller.release('f')
                time.sleep(self.interval)
                controller.press(keyboard.Key.space)
                controller.release(keyboard.Key.space)
                time.sleep(self.interval)
            else:
                time.sleep(0.1)

    def start(self):
        self.thread.start()

if __name__ == "__main__":
    key_presser = KeyPresser()
    key_presser.start()

    # Keep the main thread alive to listen for key presses
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting program")
