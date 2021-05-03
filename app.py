# import json
import json

# open json file

# error handle for inability to open or append (do for each) within each

# handle for new file

# handle for file append

# -------- #
# get input
# -------- #
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

# insert entry into list
def insertEntry(item):
    # TODO error handling needed
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

# id auto gnerated
# status code (200, 404 etc)
# page title
# url
# relative path
# parent
# children
# review notes
# -------- #
# TODO refactor this for auto item population using all values noted above. appending children isn't something that I want to focus on now
def createItem():
    item = {}
    name = input('page title')
    url = input('page url')
    status = input('status')
    item['name'] = name
    item['url'] = url
    item['status'] = status
# -------- #
# create tree
# -------- #
# TODO Organize the above information into trees while documenting
# -------- #

# print to check if correct

# append to file

# close file
