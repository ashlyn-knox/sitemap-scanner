# Sitemap Scanner
* Goal: Build a tool that will accurately map out an entire website/web application.

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

## Next Step
* implement scraper that will populate the json data instead of it being a manual tool
* Export to markdown file as a list of bullet points with limited information, export to csv file for easy visualization
