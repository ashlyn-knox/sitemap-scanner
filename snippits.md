# Code Snippits
Bits of code useful for this project

## read through keys and values of dict items in an array

for item in array:
  for key, value in item.items():
    print(key, value)
* The print van use the method .format() etc to organize how the information prints out

## adding new dict k/v pair
dictName['keyName'] = value
* This will automatically create the key and add it and the value to the object

## Reading JSON
`with open('exports/data.json', 'r') as file:
  data = file.read()

json.loads(data)`
* json.loads(data) will make the json data more readible in python, this can be assigned to a variable
* make it really easy to read with pprint
`pprint.pprint(json.loads(data))`

## format python dict as json
`json.dumps(item)`

