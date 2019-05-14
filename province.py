import requests
import function_l
province = ['https://www.tripadvisor.com/Attractions-g1308496-Activities-Chiang_Mai_Province.html',
            'https://www.tripadvisor.com/Attractions-g293920-Activities-Phuket.html',
            'https://www.tripadvisor.com/Attractions-g293916-Activities-Bangkok.html',
            'https://www.tripadvisor.com/Attractions-g2098164-Activities-Chonburi_Province.html']

def cm():
    data = requests.get(province[0])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    category=[]
    for i in soup.find_all("div",{"class":"attractions-carousel-shelf-ShelfCarouselItem__inner_wrapper--2q1xm"}) :
        for j in i.find_all('a'):
            if j.get('href').find('Activities') != -1: 
                if j.get('href').find('Chiang_Mai_Province') != -1:
                    category.append(j.get('href'))
                    print (j.get('href'))
                    print (j.text)
    print(len(category))
    #function_l.list_category(category)



def pk():
    data = requests.get(province[1])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    category=[]
    for i in soup.find_all("div",{"class":"attractions-carousel-shelf-ShelfCarouselItem__inner_wrapper--2q1xm"}) :
        for j in i.find_all('a'):
            if j.get('href').find('Activities') != -1: 
                category.append(j.get('href'))
                print (j.get('href'))
                print (j.text)
    print(len(category))
    #function_l.list_category(category)

def bk():
    data = requests.get(province[2])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    category=[]
    for i in soup.find_all("div",{"class":"attractions-carousel-shelf-ShelfCarouselItem__inner_wrapper--2q1xm"}) :
        for j in i.find_all('a'):
            if j.get('href').find('Activities') != -1: 
                category.append(j.get('href'))
                print (j.get('href'))
                print (j.text)
    print(len(category))

def ch():
    data = requests.get(province[3])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    category=[]
    for i in soup.find_all("div",{"class":"attractions-carousel-shelf-ShelfCarouselItem__inner_wrapper--2q1xm"}) :
        for j in i.find_all('a'):
            if j.get('href').find('Activities') != -1: 
                category.append(j.get('href'))
                print (j.get('href'))
                print (j.text)
    print(len(category))
    



        
