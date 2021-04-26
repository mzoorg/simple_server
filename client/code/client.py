import requests
import time

HOST_NAME = 'http://app-server'

while True:
    response = requests.get(HOST_NAME, params='ping')
    print(response.status_code, response.text)
    time.sleep(5)
