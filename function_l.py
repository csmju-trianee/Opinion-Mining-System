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
        url = ("https://"+str(link)+str(id_review[0])+"s-or"+str(i)+str(id_review[1]))
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



    

        
    



    
