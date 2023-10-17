from bs4 import BeautifulSoup
import requests

URL = "https://salemdeeds.com/salemdeeds/SaleSearch.aspx"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('td').get_text())
