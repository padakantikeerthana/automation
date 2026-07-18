import webbrowser
import time

websites = [
    "https://mail.google.com",
    "https://github.com/"
]

for site in websites:
    webbrowser.open(site)
    time.sleep(2)