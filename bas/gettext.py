import requests
def text():
    url = "https://th.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html"
    data = requests.get(url)
    from bs4 import BeautifulSoup
    num = 0
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("p",{"class":"partial_entry"})#comment
    y = soup.find_all("div",{"class":"info_text"})#name
    
    for (i,j) in zip(x,y):
        print(type(i))
        print("name : ",j.text,"\ncommnet :",i.text,"\n---------------")


    

