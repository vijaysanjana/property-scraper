import requests
from bs4 import BeautifulSoup as soup


headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
url = 'https://corp.sec.state.ma.us/corpweb/CorpSearch/CorpSearch.aspx'
# nhdeeds.org, Hillsborough county
# Send a GET request, and automatically handle SSL certificate verification
response = requests.get(url, headers=headers)


if response.status_code == 200:
    # Use BeautifulSoup to parse the HTML content
    webpage = soup(response.content, 'html.parser')
    # Now you can work with the webpage as needed
    print(webpage.prettify())  # For example, print the prettified HTML
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

