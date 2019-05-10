import requests
url ='https://www.tripadvisor.com/Attractions-g1308496-Activities-c41-Chiang_Mai_Province.html'
data = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text,'html.parser')
x = soup.find_all("a",{"class":"pageNum taLnk"},'last')
A = []
for i in x :
        if i.get('href').find('FILTERED_LIST') != -1: 
                print(i.get('href'))
