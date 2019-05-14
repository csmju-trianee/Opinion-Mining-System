import emoji
import requests
from bs4 import BeautifulSoup;
from googletrans import Translator

url = "https://www.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-or140-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html"
data = requests.get(url);
soup = BeautifulSoup(data.content,'html.parser');

name    = soup.find_all("div",{"class":"info_text"});

date    = soup.select('div.ui_column > span.ratingDate'); 
rating  = soup.select('div.ui_column > span.ui_bubble_rating');  
title   = soup.find_all("span",{"class":"noQuotes"});

comment = soup.find_all("div",{"class":"prw_rup prw_reviews_text_summary_hsx"});

#translate
translator = Translator()

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

print(a1);
print(b1);
print(c1);
print(d1);
print(e1);
