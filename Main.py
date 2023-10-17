import requests
from bs4 import BeautifulSoup as soup
from fake_useragent import UserAgent

user_agent = UserAgent()

headers={
    'User-Agent': user_agent.random,
}
url = 'https://www.masslandrecords.com/BerkMiddle/'

# Send a GET request, and automatically handle SSL certificate verification
response = requests.get(url, headers=headers)


if response.status_code == 200:
    # Use BeautifulSoup to parse the HTML content
    webpage = soup(response.content, 'html.parser')
    # Now you can work with the webpage as needed
    print(webpage.prettify())  # For example, print the prettified HTML
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
