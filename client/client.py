import requests
import time

HOST_NAME = 'http://127.0.0.1:53210'

while True:
    response = requests.get(HOST_NAME, params='ping')
    print(response.status_code, response.text)
    time.sleep(5)