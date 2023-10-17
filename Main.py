from bs4 import BeautifulSoup

html_file = """
<html>
    <body>
        <h1>Hello!</h1>
    </body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.find('h1').get_text())
