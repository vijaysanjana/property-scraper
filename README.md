# Focal Realty Property Scraper by Scope
A data scraping tool for finding when deeds transfer in Massachusetts.

## Python download:
https://www.python.org/downloads/

## All package requirements mentioned in requirements.txt file, use the following command in terminal to download the requirement:
pip install -r requirements.txt

## One of these web-drivers is required for the web scraping package to work: 
(The web-driver can exist anywhere on your computer, the web scraping package will identify its location)
(Currently using firefox driver in my implementation)

firefox-driver link:
https://github.com/mozilla/geckodriver/releases

chrome-driver link:
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

### original.py is the initial version of the project, doesn't contain a web interface
### webAppScrape.py is the latest version with the web interface for the user to choose from various options
### Note: You need to wait at least 2 minutes for the program to scrape and export a csv file, it will ask you to download the file after the program runs successfully

###Loading time: 2-3 Minutes for 100 records
