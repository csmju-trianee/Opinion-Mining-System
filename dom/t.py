
import urllib2
from bs4 import BeautifulSoup

text = """
<html>
    <head>
    </head>
    <body>
        <table>
            <p>Table1</p>
            <table>
                <p>Extra Table</p>
            </table>
        </table>
        <table>
            <p>Table2</p>
        </table>
    </body>
</html>
"""

soup = BeautifulSoup(text)

tables = soup.find('body').find_all('table')
print (len(tables))
print (tables[1].text.strip())
#3
#Extra Table # which is not the table you want without warning

tables = soup.find('body').find_all('table', recursive=False)
print (len(tables))
print (tables[1].text.strip())
#2
#Table2 # your desired output
