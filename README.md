# Sitemap Scraper

* Goal: Build a tool that will accurately map out an entire website/web application.
  - Enter root url, crawl through links and document each page connected to it
  - use link selector to find links and follow them.
    - **NOTE** This could cause problems with links to other sites, error handling needs to make sure that if the page is part of a different site, it is not to be studied
  * Track endpoints to document site.
* Output: Output information into an sql database. Or csv file. I think a db would be better
  - Create a new table for each url tree
  - id's to link them to one another
  - document data into a table. finish when everything attached to the parent url is tracked, request to go ahead with connections, create a separate table for each page group
