import requests


r = requests.get('https://httpbin.org/delay/60',timeout=3)


print(r.status_code)