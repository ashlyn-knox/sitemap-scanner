# Thinking through code writing

## Create dict
* function to create an object based off of a page
  - creates a new dict
  - takes input parameters
  - organizes input into key value pairs
  - returns the dict

## Write to JSON
* function that opens a json file to input data into
  - (separate from a function that determines if a new file will be created)
  - takes a dict
  - appends the dict to an array in a json file

### Automate search through dirtree
Currently this app is handled with manual entries, with the addition of the scraper, it will need to append data as it reads it
  - scrape along all links that have the same subdomain
  - while loop through a tree to capture depth
  - run within another loop that checks for links that go to urls of the same subdomain
    - conditional statements needed to verify when to follow links and when not -- **regex** used against urls

### Scanner flow
- Document all links in a first sweep to populate an array of all the links
- go through each link one by one.
  - repeat process for next level and so on
  - when scanning each child link, add them to the scan list index array so be used to direct the scanner at each level
