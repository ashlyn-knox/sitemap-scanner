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

# If no file already, create exports/data.json and add an array called sitemap


def write_json_entry(new_data, filename="exports/data.json"):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        # this will write to a key called siteMap. because it uses append, it will update the list/array. FOR a JSON object, use update(new_data) instead
        file_data['siteMap'].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 2)

write_json_entry(testEntry)
