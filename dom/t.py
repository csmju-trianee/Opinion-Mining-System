import requests
import re

url = "https://www.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html"
data = requests.get(url);
from bs4 import BeautifulSoup;

soup = BeautifulSoup(data.text,'html.parser');


                 
date    = soup.select('div.ui_column > span.ratingDate')         
rating  = soup.select('div.ui_column > span.ui_bubble_rating');  

for a,b in zip(date,rating):
    
    print (a.get('title'))
    print (b.get('class')[1].split('bubble_')[1].split('0')[0])
    print ("*************************************\n");

