import requests
import json 
for i in range(1,13):
	payload = {'page' : i}
	r = requests.get('https://reqres.in/api/users?',params = payload).json()
	print(r)
	r1 = r['data']
	print(sum(1 if d['id'] else 0 for d in r1))
# r = requests.get("https://coderbyte.com/api/challenges/json/age-counting")
# print(r.json()['data'].split(','))
