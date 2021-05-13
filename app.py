# import json
import csv
import json
import os

# Directory Management
def create_output_dir():
    # check if the default dir already exists
    default_dir = ('exports')
    # if not
    if not os.path.isdir(default_dir):
        # TODO ask user if default dir is ok
        # IF yes mkdir exports in current directory
        os.mkdir(default_dir)
        print("created directory", default_dir)
        # TODO else get a directory specified by the user
    else:
        print("directory already exists")

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

# TODO create content relative filename based on url

# JSON Oput function
def write_json_entry(new_data, filename="exports/data.json"):
    with open(filename, 'r+') as json_file:
        json_file_data = json.load(file)
        # NOTE this will write to a key called siteMap. because it uses append, it will update the list/array. FOR a JSON object, use update(new_data) instead
        json_file_data['siteMap'].append(new_data)
        json_file.seek(0)
        json.dump(json_file_data, json_file, indent = 2)

# csv output function
def write_csv_entry(new_data, filename="exports/data.csv"):
    with open(filename, 'r+') as csv_file:
        csv_writer = csv.writer(csv_file)
        # Write column labels
        csv_writer.writerow(["name",
                             "url",
                             "subdomain",
                             "top-level",
                             "children",
                             "links"])
        # TODO Itrate through scraped data and add to rows
        # if list is not empty
        if pages.get("items") is not None:
            for page in pages.get("items"):
                page_data_row = [
                    # TODO Set up scraper to add to list and send information to this function
                    page[null][null].encode("utf-8"),
                    page[null][null].encode("utf-8")
                ]
                csv.writer.writerow(page_data_row)
                # TODO handle pagination
# TODO put into a while True loop to add multiple pages
write_json_entry(pageEntry())
