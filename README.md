# Sitemap Scanner
* Goal: Build a tool that will accurately map out an entire website/web application.

## Manual Input and basic setup
- [ ] Refactor to use class template for each page
- [ ] CLI for manual data entry
- [ ] Organize data by lists that denote site hierarchy levels **handle pages that are children of only 1 page**
- [ ] manual entry verification setup - input a page and then confirm correct input **first phase, append to file on entry verification**
  - second phase, option to append after entry of whole list, use a look to push list items to the file
- [ ] refactor code to separate files for easier maintainability
- [X] create directory output function
- [X] page Entry function to take user input
- [X] JSON output function
- [X] CSV output function

## Output
* implement scraper that will populate the json data instead of it being a manual tool
* Export to markdown file as a list of bullet points with limited information, export to csv file for easy visualization
* **IMPORTANT** tree display output like (this)[https://gist.github.com/acidtone/b4cdb0741460d54f5966ab18a753548c]

## Resources
* (Python directory tree generator)[https://realpython.com/directory-tree-generator-python/]
