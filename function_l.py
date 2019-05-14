import requests
import link_l
import datetime
import pymysql.cursors
from googletrans import Translator

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

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
        name    = soup.select('div.info_text');
        date    = soup.select('div.ui_column > span.ratingDate'); 
        rating  = soup.select('div.ui_column > span.ui_bubble_rating');  
        title   = soup.find_all("span",{"class":"noQuotes"});
        comment = soup.find_all("div",{"class":"prw_rup prw_reviews_text_summary_hsx"});

        #translate
        translator = Translator()

        #attribute count
        q = len(name)
        w = len(date)
        e = len(rating)
        r = len(title)
        t = len(comment)
        print("count: name=",q,"date=",w,"rating=",e,"title=",r,"comment=",t,"\n")

        for a,b,c,d,e in zip(name,date,rating,title,comment):
            a1 = a.text
            b1 = translator.translate(b.get('title'),dest='en').text
            c1 = c.get('class')[1].split('bubble_')[1].split('0')[0]
            d1 = d.text 
            e1 = e.text
            e2 = e1.encode("ascii", "ignore")
    
            if b1[0].isdigit():
                obj = datetime.datetime.strptime(str(b1),'%d %B %Y')
            else:
                obj = datetime.datetime.strptime(str(b1),'%B %d, %Y')
    
            print("Name:",a1)
            print("Date:",obj.date())
            print("Rating:",c1+"/5")
            print("Title:",translator.translate(d1,dest='en').text)
            print("Description:",e2)

            print("*************************************\n");
            
            try:
                with connection.cursor() as cursor:

                #sql_del = "DELETE FROM data"
                #cursor.execute(sql_del)
                #connection.commit()
                    for a,b,c,d,e in zip(name,date,rating,title,comment):
                        a1 = a.text
                        b1 = translator.translate(b.get('title'),dest='en').text
                        c1 = c.get('class')[1].split('bubble_')[1].split('0')[0]
                        d1 = translator.translate((d.text),dest='en').text
                        e1 = translator.translate((e.text),dest='en').text
                        if b1[0].isdigit():
                            obj = datetime.datetime.strptime(str(b1),'%d %B %Y')
                        else:
                            obj = datetime.datetime.strptime(str(b1),'%B %d, %Y')
                
                        b2 = obj.date()
            
                sql = "INSERT INTO `data` (`name`,`date`,`rating`,`title`,`descript`) VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql,(a1,b2,c1,d1,e1))
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
    location_name=[]
    list_review=[]
    for i in list_page : 
        url = i
        #print(url)
        data = requests.get(url)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(data.text,'html.parser')
        for i in soup.find_all('div',{'class':'listing_title'} ):
             for j in i.find_all('a'):
                    location_name.append(j.text)
                    list_review.append("https://www.tripadvisor.com"+j.get('href'))
    return(list_review, location_name)

def list_category(category):
    list_start=[]
    list_name=[]
    try:
        li_category = category
        for i in li_category : 
            url = ('https://www.tripadvisor.com' + i)
            list_start ,list_name = Max_category(url)
        #insert sql
            with connection.cursor() as cursor:
                    for j,k in zip(list_name,list_start) :
                        sql = "INSERT INTO `location`(`l_name`, `url`) VALUES (%s,%s)"
                        cursor.execute(sql,(j,k))
                    connection.commit()
    finally:
                print("stop insesrt")
                connection.close()


    
                    



       
    


