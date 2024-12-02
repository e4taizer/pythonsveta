import requests
url = 'https://catfact.ninja/fact'
headers = {
'accept': 'application/json',
'X-CSRF-TOKEN': 'YwUNsltGgGLyvF1egz8o8DaEWkZHC9lFYWVgsHXs'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Ошибка при запросе: {response.status_code}")