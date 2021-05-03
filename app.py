# import json
import json
import pprint

# Data list
data = []

# SAMPLE DATA
testEntry = {
    'name': 'Get Fedora Landing Page',
    'url': 'https://getfedora.org',
    'subdomain': '',
    'second-level': 'getfedora',
    'top-level': 'org',
    'children': ['workstation', 'server', 'iot'],
    'links': ['fedoraproject.org', 'docs.fedoraproject.org'],
    'status': '200',
    'notes': ''
}

def createItem():
    item = {}
    name = input('page title: ')
    url = input('page url: ')
    status = input('status: ')
    item['name'] = name
    item['url'] = url
    item['status'] = status
    return item

# TODO refactor this for auto item population using all values noted above. appending children isn't something that I want to focus on now

# insert entry into list
def insertEntry(item):
    # TODO error handling needed
    createItem()
    # check if the item is ok
    pprint.pprint(item)
    while True:
        try:
            verifyItem = input('Does anything need to be change? yes or no')
            if verifyItem == 'y':
                # TODO use the object.update() method to change keys
                print('placeholder for function to change content')
            else:
                # Append to the list
                data.append(item)
                print('successful insertion')
            break
        except ValueError:
            print('There was a value error')

# ------------------ #
# Write to json file
# ------------------ #

while True:
    try:
        # create a new file set to append. TODO create a more useful filename sequence
        # TODO add from data list that will be auto populated. **ATM** design for manual entry append
        file = open('export/data.json', 'a')
        # TODO run a loop to append content to the file

        # close file when finished adding
        file.close()
    except FileNotFoundError:
        print('Could not find the file that you\'re trying to write to')

