import requests
from bs4 import BeautifulSoup as soup


headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
url = ''
# https://ava.fidlar.com/NHHillsborough/AvaWeb/#/search for Hillsborough County, NH
# Send a GET request, and automatically handle SSL certificate verification
response = requests.get(url, headers=headers)

def main():
    if response.status_code == 200:
    # Use BeautifulSoup to parse the HTML content
        webpage = soup(response.content, 'html.parser')
    # Now you can work with the webpage as needed
        print(webpage.prettify())  # For example, print the prettified HTML
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    return

def isLLC():
    # Search through public LLC records to verify whether an entity is a verified LLC
    return
def toCSV():
    # parse through HTML and retrieve necessary data
    return

def getPrice():
    # cross reference property with Zillow/another home search service to obtain price at which it was sold
    return

if __name__ == "__main__":
    main()