import requests
import json
url = 'https://my-json-server.typicode.com/typicode/demo/posts'
r1 = requests.get(url)
r2 = r1.json()
r3 = requests.get('https://my-json-server.typicode.com/typicode/demo/comments')
r4 = r3.json()
with open("names.json","w") as f:
	dict1 = json.dumps(r2)
	dict2 = json.dumps(r4)
	f.write(dict1)
	f.write('\n')
	f.write(dict2)
