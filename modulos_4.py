#pip install requests
import requests
respuesta = requests.get('https://www.google.com')
print(respuesta.text)