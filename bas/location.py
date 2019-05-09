import requests
def Maximum_page():
    url = "https://www.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html"
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"class":"pagination-details"},"b")#Maximum
    for i in x:
        print(i.text[9:13])
    
        
