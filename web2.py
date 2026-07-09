import time

try:
    import pyautogui
except ImportError:
    print("pyautogui is not installed. Install it with: pip install pyautogui")
    raise SystemExit(1)

time.sleep(5)  # Time to switch to the target window

pyautogui.write("Hello, this is automated typing!", interval=0.1)
pyautogui.press("enter")