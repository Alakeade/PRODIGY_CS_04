# Keylogger Program 

This repository contains a basic keylogger program designed for educational purposes. It records keystrokes and logs them into a file for analysis. **This tool is strictly for authorized use and educational environments. Misuse of keyloggers can result in severe legal consequences.**

## Features

- **Logs Keystrokes**: Records all keystrokes, including special keys like `Enter`, `Space`, and `Backspace`.
- **File Logging**: Saves logged keys to a specified file (`keylog.txt`).
- **Graceful Exit**: Stops logging when the `Escape` key is pressed.

## Requirements

- Python 3.7 or higher
- `pynput` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/keylogger.git
   ```
2. Navigate to the project directory:
   ```bash
   cd keylogger
   ```
3. Install the required dependencies:
   ```bash
   pip install pynput
   ```

## Usage

1. Run the program:
   ```bash
   python keylogger.py
   ```
2. Press the `Escape` key to stop the keylogger.

### Log File

The keystrokes will be saved in a file named `keylog.txt` in the same directory as the script.

### Example Log Output
```
[SPACE]Hello[BACKSPACE][SPACE]World[ENTER]
```

## Ethical Notice

- **Authorized Use Only**: This program must not be deployed without the explicit consent of all parties involved.
- **Legal Compliance**: Ensure you comply with all applicable laws and regulations in your jurisdiction.
- **Educational Purpose**: This program is intended solely for learning purposes, such as understanding cybersecurity principles.

## File Structure

- `keylogger.py`: The main script for recording keystrokes.
- `keylog.txt`: File where the logged keys are stored.
- `README.md`: Documentation for the project.


