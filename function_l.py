import requests
import link_l
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
def value_page(Url):
    #function Max review
    url = ("https://www.tripadvisor.com"+str(Url))
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("span",{"class":"reviews_header_count"})
    for i in x:
        ch = i.text
        number = (int(ch.strip( '()' )))
        return(int(number-10))
        break
    #break เผื่อเอาท้ายเดี่ยว
    
def getlink(Url):
    url = str("https://www.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html")
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("a",{"class":"pageNum last taLnk"},"href=")
    for i in x:
     return(i.get('href'))
     break

def getText(link,id_review,Maxpage):
    start = Maxpage
    pages=[]
    for i in range(int(start),-1,-10):
        url = ("https://"+str(link)+str(id_review[0])+"Reviews-or"+(str(i).replace(",", ""))+"-"+str(id_review[1]))
        pages.append(url)
    for datalink in pages:
        page = requests.get(datalink)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page.text,'html.parser')
        x = soup.find_all("p",{"class":"partial_entry"})#comment
        y = soup.find_all("div",{"class":"info_text"})#name
    
        for (i,j) in zip(x,y):
            print(datalink)
            print("name : ",j.text,"\ncommnet :",(i.text).encode('UTF-8'),"\n---------------")

def list_category(category):
    try:
        li_category = category
        for i in li_category : 
            url = ('https://www.tripadvisor.com' + i)
            list_start = Max_category(url)
        #insert sql
            with connection.cursor() as cursor:
                    for j in list_start :
                        sql = "INSERT INTO `Location`(`url`) VALUES (%s)"
                        cursor.execute(sql,j)
                    connection.commit()
    finally:
                connection.close()
def Max_category(urls):
   #function Max review
    url = urls
    list_page=[]
    list_page.append(url)
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x  = soup.find_all("a",{"class":"pageNum taLnk"})
    for i in x :
            if i.get('href').find('FILTERED_LIST') != -1: 
                list_page.append("https://www.tripadvisor.com"+i.get('href'))

    list_review=[]
    for i in list_page : 
        url = i
        print(url)
        data = requests.get(url)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(data.text,'html.parser')
        for i in soup.find_all('div',{'class':'listing_title'} ):
             for j in i.find_all('a'):
                    list_review.append("https://www.tripadvisor.com"+j.get('href'))
    print(list_review)
    return(list_review)
    
                    



       
    


