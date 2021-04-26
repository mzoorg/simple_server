import requests
import time

HOST_NAME = 'http://172.17.0.2:53210'

while True:
    response = requests.get(HOST_NAME, params='ping')
    print(response.status_code, response.text)
    time.sleep(5)
