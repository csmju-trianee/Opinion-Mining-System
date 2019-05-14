import requests
url = 'https://www.tripadvisor.com/Attraction_Review-g293917-d16874316-Reviews-Student_Night_Market-Chiang_Mai.html'

data = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text,'html.parser')
x = soup.find_all("div",{"data-value":"ko"},"span")
try:
    for i in x:
       txt = str(i.text.split('(')[1].split(')')[0])
       newstr = txt.replace(",", "")
       print(i.text)
       break
except:
        pass
        print("pass")
        
        