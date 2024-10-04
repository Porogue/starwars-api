import requests
import time

url = "http://0.0.0.0:8000/fetch"

for i in range(5):
    requests.get(url)
    time.sleep(5)
