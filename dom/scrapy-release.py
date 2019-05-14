import requests
import datetime
import pymysql.cursors
from googletrans import Translator
from bs4 import BeautifulSoup;

url = "https://www.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-or40-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html"
data = requests.get(url);

soup = BeautifulSoup(data.content,'html.parser');

name    = soup.select('div.info_text');
date    = soup.select('div.ui_column > span.ratingDate'); 
rating  = soup.select('div.ui_column > span.ui_bubble_rating');  
title   = soup.find_all("span",{"class":"noQuotes"});

comment = soup.find_all("div",{"class":"prw_rup prw_reviews_text_summary_hsx"});

#translate
translator = Translator()

#attribute count
q = len(name);
w = len(date);
e = len(rating);
r = len(title);
t = len(comment);
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
    
    print("Name:",a1);
    print("Date:",obj.date());
    print("Rating:",c1+"/5");
    print("Title:",translator.translate(d1,dest='en').text);
    print("Description:",e2);

    print("*************************************\n");
    
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:

        sql_del = "DELETE FROM data"
        cursor.execute(sql_del)
        connection.commit()
        
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









