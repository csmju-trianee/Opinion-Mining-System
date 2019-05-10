import requests

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
     #print(i.get('href'))
     return(i.get('href'))
     break

def getText(link,id_review,Maxpage):
    start = int(Maxpage)
    i=start
    stop = 0 
    step = -10
    pages=[]
    for i in range(start,stop,step):
        url = ("https://"+str(link)+str(id_review[0])+"Reviews-or"+str(i)+"-"+str(id_review[1]))
        pages.append(url)
    for datalink in pages:
        page = requests.get(datalink)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page.text,'html.parser')
        x = soup.find_all("p",{"class":"partial_entry"})#comment
        y = soup.find_all("div",{"class":"info_text"})#name
    
        for (i,j) in zip(x,y):
            print(datalink)
            print("name : ",j.text,"\ncommnet :",i.text,"\n---------------")

def list_category(category):
    datalink='https://www.tripadvisor.com/Attractions-g1308496-Activities-c41-Chiang_Mai_Province.html'
    A = datalink.split('https://www.tripadvisor.com/')
    Max_ca = Max_category(A)
    print(Max_ca)
    #ทำต่อ เชื่อม code
    page = requests.get(datalink)
    from bs4 import BeautifulSoup    
    soup = BeautifulSoup(page.text,'html.parser')
    x = soup.find_all("a")#comment
    link = []
    for i in x :
        if i.get('href').find('#REVIEWS') != -1: 
            link.append(i.get('href'))
            print(i.get('href'))

def Max_category():
   #function Max review
    #url = ("https://www.tripadvisor.com"+str(Url))
    url ='https://www.tripadvisor.com/Attractions-g1308496-Activities-c41-Chiang_Mai_Province.html'
    list_review=[]
    list_review.append(url)
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x  = soup.find_all("a",{"class":"pageNum taLnk"})
    for i in x :
            if i.get('href').find('FILTERED_LIST') != -1: 
                list_review.append("https://www.tripadvisor.com"+i.get('href'))
    
    for i in list_review : 
        url = i
        print(url)
        data = requests.get(url)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(data.text,'html.parser')

                    
        for i in soup.find_all('div',{'class':'listing_title'} ):
             for j in i.find_all('a'):
                    j.get('href')

def Reviews_select(list_review):
    list_page=[] 
    list_page= list_review
    for i in list_page :
        url = "www.tripadvisor.com"+i
        print(url)
        data = requests.get(url)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(data.text,'html.parser')
        x  = soup.find_all("a")
        for i in x :
                print(i.get('href'))


       
    


