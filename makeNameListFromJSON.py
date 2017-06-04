import yaml

with open("anniklasDatabase.json", "r") as fp:
	jso = fp.read()
	jso = yaml.load(jso.decode('utf-8', 'ignore'))
	print(jso)
