import json
from urllib.request import urlopen

with open('data.json') as f:
	data = json.load(f)

for state in data['states']:
	del state['abbreviation']

with open('new_states.json', 'w') as f:
	json.dump(data, f, indent=2)

#grab a api and use it to seperate data

with urlopen("https://cat-fact.herokuapp.com/facts") as response:
	source = response.read()

data = json.loads(source)

print("-" * 35, '\n')
print("Here is the raw json: \n")
print("-" * 35, '\n')

print(json.dumps(data, indent=2))

print("-" * 35, '\n')
print("Here are the random cat facts: \n")
print("-" * 35, '\n')

for fact in data:
	print(fact['text'], '\n')