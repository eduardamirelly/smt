import requests
import datetime

#na matricula colocando matricula que existe e não existe
#lembrar de rodar o comando: pip install -r requeriments.txt

payload = {'matriculation': '20191104010026', 'dt_enter': datetime.datetime.now() }
r = requests.get('http://127.0.0.1:8000/entry/', params=payload)
print(r.status_code)
print(r.url)
print(r.text)
