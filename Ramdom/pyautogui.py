import threading
import time
import os
import win32api
import win32con
import keyboard

class KeyPresser:
    def __init__(self):
        self.is_active = False
        self.interval = 0.1  # Time interval in seconds
        self.toggle_key = 't'  # Toggle key
        self.exit_key = 'esc'  # Exit key

    def start(self):
        self.thread = threading.Thread(target=self.press_keys)
        self.thread.daemon = True
        self.thread.start()

        keyboard.on_press_key(self.toggle_key, self.toggle)
        keyboard.on_press_key(self.exit_key, self.exit)

        print(f"Press '{self.toggle_key}' to start/stop the macro.")
        print(f"Press '{self.exit_key}' to exit.")

    def toggle(self, event):
        self.is_active = not self.is_active
        if self.is_active:
            print("Macro started")
        else:
            print("Macro stopped")

    def exit(self, event):
        print("Exiting...")
        self.is_active = False
        time.sleep(0.5)
        os._exit(0)

    def press_keys(self):
        while True:
            if self.is_active:
                win32api.keybd_event(0x46, 0, 0, 0)  # 'f' key down
                time.sleep(self.interval)
                win32api.keybd_event(0x46, 0, win32con.KEYEVENTF_KEYUP, 0)  # 'f' key up
                win32api.keybd_event(0x20, 0, 0, 0)  # Space key down
                time.sleep(self.interval)
                win32api.keybd_event(0x20, 0, win32con.KEYEVENTF_KEYUP, 0)  # Space key up
            else:
                time.sleep(0.1)

if __name__ == "__main__":
    key_presser = KeyPresser()
    key_presser.start()

    # Keep the main thread alive to listen for key presses
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting program")
