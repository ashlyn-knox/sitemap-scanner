# Sitemap Scanner
* Goal: Build a tool that will accurately map out an entire website/web application.
* **NOTE** -- write to file within function or after function is run

## Progress
* Currently creating function to create a json file and populate it with entries. Each entry will be a page.
* **TODO** decide how to document tree structure. This is my current idea -- however I'm considering switching from JSON to SQL
  - create a list for each subdomain
  - populate list with objects, an object will contain all the information for  given page (including other subdomains that it links to and it's children)
  - Test this out, as sites become really nested, this system may become unintuitive to parse.
* Automatically write entries to the json file
* Improve error handling and user interface
  - verification of correct entry
  - ability to update entries prior to submitting them

## Next Steps (as of3-05-21)
* implement scraper that will populate the json data instead of it being a manual tool
* error handling for input, enforce consistency of how things are written, and make sure data types are correct
* Export to markdown file as a list of bullet points with limited information, export to csv file for easy visualization
* **IMPORTANT** tree display output like (this)[https://gist.github.com/acidtone/b4cdb0741460d54f5966ab18a753548c]

## Resources
* (Python directory tree generator)[https://realpython.com/directory-tree-generator-python/]
