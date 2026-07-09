import webbrowser
import time

websites = [
    "https://www.google.com",
    "https://github.com",
    "https://www.linkedin.com"
]

for site in websites:
    webbrowser.open(site)
    time.sleep(2)