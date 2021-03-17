import requests
import datetime

#na matricula colocando matricula que existe e não existe
#lembrar de rodar o comando: pip install -r requeriments.txt

payload = {'student': '2020121212', 'dtenter': datetime.datetime.now() }
r = requests.get('http://127.0.0.1:8000/entrada', params=payload)
print(r.status_code)
print(r.text)
