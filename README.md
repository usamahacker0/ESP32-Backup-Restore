# ESP32 Backup and Restore

![esp32 backup and restore](https://github.com/user-attachments/assets/e46daf78-4022-4dd5-895d-e214d5b0a26b)

## Requirements

- Download the latest version of Python:

  [![Download Latest Python](https://img.shields.io/badge/Download-Python-blue)](https://www.python.org/downloads/)

- `esptool.py` is required to run this application. Follow the steps below to install it.

## How to Install `esptool`

1. **Ensure Python is installed:**
   - Download and install the latest version of Python from the link above.
   - Verify the installation by opening a terminal or command prompt and running:
     ```bash
     python --version
     ```
   - If you are using Python 3, you might need to use `python3` instead of `python` in the commands below.

2. **Install `pip` (if not already installed):**
   - `pip` usually comes with Python, but you can ensure it's installed by running:
     ```bash
     python -m ensurepip --upgrade
     ```

3. **Install `esptool`:**
   - Open a terminal or command prompt.
   - Run the following command to install `esptool` using `pip`:
     ```bash
     pip install esptool
     ```
   - Verify the installation by running:
     ```bash
     esptool.py --version
     ```
