import json
name = 'בנק הפועלים'



data = open("data.json","r").read()
steps = json.loads(data)[name]
i = 1
for step in steps:
    commands = step["commands"]
    for command in commands:
        print (command)