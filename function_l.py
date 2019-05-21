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

def getText(link,id_review,Maxpage,province):
    start = Maxpage
    pages=[]
    p = province
    for i in range(int(start),-1,-10):
        url = ("https://"+str(link)+str(id_review[0])+"Reviews-or"+(str(i).replace(",", ""))+"-"+str(id_review[1]))
        pages.append(url)
    for datalink in pages:
        print(datalink)
        page = requests.get(datalink)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page.text,'html.parser')
        name    = soup.select('div.info_text')
        date    = soup.select('div.ui_column > span.ratingDate')
        rating  = soup.select('div.ui_column > span.ui_bubble_rating')
        title   = soup.find_all("span",{"class":"noQuotes"})
        comment = soup.find_all("div",{"class":"prw_rup prw_reviews_text_summary_hsx"})
        #translate
        translator = Translator()
        #attribute count
        # q = len(name)
        # w = len(date)
        # e = len(rating)
        # r = len(title)
        # t = len(comment)
        #print("count: name=",q,"date=",w,"rating=",e,"title=",r,"comment=",t,"\n")
        try:
                with connection.cursor() as cursor:
                    for a,b,c,d,e in zip(name,date,rating,title,comment):
                        a1 = a.text
                        #b1 = translator.translate(b.get('title'),dest='en').text
                        c1 = c.get('class')[1].split('bubble_')[1].split('0')[0]
                        #d1 = translator.translate((d.text),dest='en').text
                        e1 = e.text
                        #e2 = e1.encode("ascii", "ignore")
                        try:
                            e3 = translator.translate((e1),dest='en').text
                        except :
                            e3 = e1
           
            
                        # if b1[0].isdigit():
                        #     obj = datetime.datetime.strptime(str(b1),'%d %B %Y')
                        # else:
                        #     obj = datetime.datetime.strptime(str(b1),'%B %d, %Y')
            
                        # b2 = obj.date()
                        b2 ="2018-07-14"
                        d1 ="5"
                        #print("Name:",a1)
                        #print("Date:",b2)
                        #print("Rating:",c1+"/5")
                        #print("Title:",translator.translate(d1,dest='en').text)
                        #print("Description:",e2);
                        print("*************************************\n")
            
                        sql = "INSERT INTO `data` (`province`,`name`,`date`,`rating`,`title`,`descript`) VALUES (%s,%s,%s,%s,%s,%s)"
                        cursor.execute(sql,(province,a1,b2,c1,d1,e3))
                connection.commit()
        finally:
            print("inserted")
            #connection.close()


def list_category(category,p_id):
    p = p_id
    try:
       
        li_category = category
        for j in li_category :
            url = ('https://www.tripadvisor.com' + j)
            newMax_category(url,p)

    #     for i in li_category : 
    #         url = ('https://www.tripadvisor.com' + i)
    #         list_start ,list_name = newMax_category(url)
        
    #         with connection.cursor() as cursor:
    #                 for j,k in zip(list_name,list_start) :
    #                     sql = "INSERT INTO `location`(`l_name`, `url`, `Province`,`cateID`) VALUES (%s,%s,%s,%s)"
    #                     cursor.execute(sql,(j,k,p,'2'))
    #                 connection.commit()
    finally:
                print("finally insert url .")
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
    

def newMax_category(url,p):
        p_id = p
        print(url)
        urls = url
        list_page=[]
        location_name =[]
        list_review=[]
        data = requests.get(urls)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(data.text,'html.parser')
        x  = soup.find_all("a",{"class":"pageNum taLnk"})
        for i in x :   
            #if i.get('href').find('#FILTERED_LIST') != -1: 
            list_page.append(i.get('href'))
        
        list_page.reverse() 
        print(len(list_page))

        if len(list_page)==0:
            data = requests.get(url)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(data.text,'html.parser')
            x = soup.find_all('div',{'class': 'listing_title'})
            for i in x :
                for j in i.find_all('a',):
                    location_name.append(j.text)
                    list_review.append("https://www.tripadvisor.com"+j.get('href'))

            
            with connection.cursor() as cursor:
                for j,k in zip(location_name,list_review) :
                    sql = "INSERT INTO `location`(`l_name`, `url`, `Province`) VALUES (%s,%s,%s)"
                    cursor.execute(sql,(j,k,p_id))
                connection.commit()


        if len(list_page) > 1 :
                id_review  = list_page[0].split('oa')[1].split('-')
                link = list_page[0].split('-oa')
                pages=[]
                for i in range(int(id_review[0]),-1,-30):
                    url = ("https://www.tripadvisor.com"+str(link[0])+"-oa"+(str(i).replace(",", ""))+"-"+str(id_review[1]))
                    pages.append(url)

                for i in pages : 
                    print(i)
                    data = requests.get(i)
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(data.text,'html.parser')
                    for k in soup.find_all('div',{'class':'listing_title'} ):
                        for j in k.find_all('a',):
                            location_name.append(j.text)
                            list_review.append("https://www.tripadvisor.com"+j.get('href'))

        with connection.cursor() as cursor:
            for j,k in zip(location_name,list_review) :
                sql = "INSERT INTO `location`(`l_name`, `url`, `Province`) VALUES (%s,%s,%s)"
                cursor.execute(sql,(j,k,p_id))
                connection.commit()


                    



       
    


