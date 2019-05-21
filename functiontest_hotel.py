import pymysql
import threading

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
import requests
url = 'https://www.tripadvisor.com/Hotels-g2098164-Chonburi_Province-Hotels.html'
list_page=[]
data = requests.get(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text,'html.parser')
x  = soup.find_all("a")
for i in x :   
    if i.get('href').find('#BODYCON') != -1: 
        list_page.append(i.get('href'))

list_page.reverse()
location_name = []
list_review=[]

id_review  = list_page[0].split('oa')[1].split('-')
link = list_page[0].split('-oa')
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
p = 'Chonburi'
try:
                with connection.cursor() as cursor:
                    for j,k in zip(location_name,list_review) :
                        sql = "INSERT INTO `location`(`l_name`, `url`, `Province`,`cateID`) VALUES (%s,%s,%s,%s)"
                        cursor.execute(sql,(j,k,p,'1'))
                    connection.commit()
finally:
                print("stop insesrt")
                connection.close()
