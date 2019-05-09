from bs4 import BeautifulSoup
html = '<p>Hello</p> <p>world</p>'
soup = BeautifulSoup(html, 'lxml')
