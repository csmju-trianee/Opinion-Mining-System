import requests
import page_number
from multiprocessing import Process
import function_l
import pymysql
import threading
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                             
location_name = []
list_review=[]
url = 'https://www.tripadvisor.com/Attractions-g1308496-Activities-c57-Chiang_Mai_Province.html'
print(url)
data = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text,'html.parser')
x = soup.find_all('a',{"class":"pageNum taLnk"})
for i in x :
        location_name.append(i.text)
        list_review.append(i.get('href'))

print(len(list_review))
print(len(location_name))
print(list_review)

list_review.reverse()


id_review  = list_review[0].split('oa')[1].split('-')
link = list_review[0].split('-oa')
#print(id_review[1])
#print(list_page[0])
#print(link)
pages=[]

for i in range(int(id_review[0]),-1,-30):
    url = ("https://www.tripadvisor.com"+str(link[0])+"-oa"+(str(i).replace(",", ""))+"-"+str(id_review[1]))
    pages.append(url)

print(pages)
for i in pages : 
    url = i
    print(url)
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    for i in soup.find_all('div',{'class':'listing_title'} ):
        for j in i.find_all('a',):
            location_name.append(j.text)
            list_review.append("https://www.tripadvisor.com"+j.get('href'))
print(location_name)


list_start=list_review
list_name=location_name