import requests
import datetime
from googletrans import Translator
from bs4 import BeautifulSoup;

url = "https://www.tripadvisor.com/AttractionProductReview-g293917-d12089507-Doi_Suthep_Temple_and_Bau_Thong_Waterfalls_Private_Tour-Chiang_Mai.html"
data = requests.get(url);

soup = BeautifulSoup(data.text,'html.parser');

name    = soup.find_all("div",{"class":"info_text"});                   
date    = soup.select('div.ui_column > span.ratingDate'); 
rating  = soup.select('div.ui_column > span.ui_bubble_rating');  
title   = soup.find_all("span",{"class":"noQuotes"});   
comment = soup.find_all("div",{"class":"prw_rup prw_reviews_text_summary_hsx"});         #ความคิดเห็น

#translate
translator = Translator()
ex = translator.translate('รีวิวเมื่อ 14 มีนาคม ค.ศ. 2019')
print (ex.text)

#datetime
date_time_str = 'september 13 2018'  
if date_time_str[0].isdigit():
    date_time_obj = datetime.datetime.strptime(date_time_str,'%d %B %Y')
else:
    date_time_obj = datetime.datetime.strptime(date_time_str,'%B %d %Y')

print('Date:', date_time_obj.date())  
print ('Current date/time: {}'.format(datetime.datetime.now()))

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

    if b1[0].isdigit():
        obj = datetime.datetime.strptime(str(b1),'%d %B %Y')
    else:
        obj = datetime.datetime.strptime(str(b1),'%B %d, %Y')
    
    print("Name:",a1);
    print("Date:",obj.date());
    print("Rating:",c1+"/5");
    print("Title:",translator.translate(d1,dest='en').text);
    print("Descript:",translator.translate(e1,dest='en').text);

    print("*************************************\n");
    
