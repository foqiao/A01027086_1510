import json

"""
read more here:
https://docs.python.org/3.8/library/json.html
"""

with open('input.json', 'r') as data:
	obj = json.load(data)
	with open('output.txt', 'w') as output:
		output.write(obj['name'] + "'s Hobbies:\n")
		for hobby in obj['hobbies']:
			output.write(hobby + "\n")

