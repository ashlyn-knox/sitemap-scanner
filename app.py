# import json
import json

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

# Manual data input funciton
def pageEntry():
    page_data = {}
    page_data['name'] = input('h1: ')
    page_data['url'] = input('url: ')
    page_data['subdomain'] = input('subdomain: ')
    page_data['top-level'] = input('top-level: ')
    page_data['children'] = []
    while True:
        user_input = input('enter child url (type done when finished): ')
        if user_input != "done":
            page_data['children'].append(user_input)
        else:
            break
    # TODO Create loops to add multiple links
    page_data['links'] = []
    while True:
        user_input = input('enter link url (type done when finished): ')
        if user_input != "done":
            page_data['links'].append(user_input)
        else:
            break
    page_data['status'] = int(input('status: '))
    return page_data

# If no file already, create exports/data.json and add an array called sitemap

def write_json_entry(new_data, filename="exports/data.json"):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        # NOTE this will write to a key called siteMap. because it uses append, it will update the list/array. FOR a JSON object, use update(new_data) instead
        file_data['siteMap'].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 2)

# TODO put into a while True loop to add multiple pages
write_json_entry(pageEntry())
