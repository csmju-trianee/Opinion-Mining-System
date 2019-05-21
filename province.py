import requests
import function_l
import multiprocessing 
from multiprocessing import Process
attraction = ['https://www.tripadvisor.com/Attractions-g1308496-Activities-Chiang_Mai_Province.html',
            'https://www.tripadvisor.com/Attractions-g293920-Activities-Phuket.html',
            'https://www.tripadvisor.com/Attractions-g293916-Activities-Bangkok.html',
            'https://www.tripadvisor.com/Attractions-g2098164-Activities-Chonburi_Province.html']

restaurants = ['https://www.tripadvisor.com/Restaurants-g293917-Chiang_Mai.html',
                'https://www.tripadvisor.com/Restaurants-g293920-Phuket.html',
                'https://www.tripadvisor.com/Restaurants-g293916-Bangkok.html',
                'https://www.tripadvisor.com/Restaurants-g2098164-Chonburi_Province.html']

hotel = ['https://www.tripadvisor.com/Hotels-g1308496-Chiang_Mai_Province-Hotels.html',
        'https://www.tripadvisor.com/Hotels-g293920-Phuket-Hotels.html',
        'https://www.tripadvisor.com/Hotels-g293916-Bangkok-Hotels.html',
        'https://www.tripadvisor.com/Hotels-g2098164-Chonburi_Province-Hotels.html']
                

def cm():
    data = requests.get(attraction[0])
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
    p_id = 'ChiangMai'
    function_l.list_category(category,p_id)



def pk():
    data = requests.get(attraction[1])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    category=[]
    for i in soup.find_all("div",{"class":"attractions-carousel-shelf-ShelfCarouselItem__inner_wrapper--2q1xm"}) :
        for j in i.find_all('a'):
            if j.get('href').find('Activities') != -1: 
                category.append(j.get('href'))
                print (j.get('href'))
                print (j.text)
    p_id = 'Phuket'
    function_l.list_category(category,p_id)


def bk():
    data = requests.get(attraction[2])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    category=[]
    for i in soup.find_all("div",{"class":"attractions-carousel-shelf-ShelfCarouselItem__inner_wrapper--2q1xm"}) :
        for j in i.find_all('a'):
            if j.get('href').find('Activities') != -1: 
                category.append(j.get('href'))
                print (j.get('href'))
                print (j.text)
    p_id = 'Bangkok'
    function_l.list_category(category,p_id)

def ch():
    data = requests.get(attraction[3])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    category=[]
    for i in soup.find_all("div",{"class":"attractions-carousel-shelf-ShelfCarouselItem__inner_wrapper--2q1xm"}) :
        for j in i.find_all('a'):
            if j.get('href').find('Activities') != -1: 
                category.append(j.get('href'))
                print (j.get('href'))
                print (j.text)
    p_id = 'Chonburi'
    function_l.list_category(category,p_id)
    
    

if __name__ == '__main__':
   p1 = Process(target=cm)
   p2 = Process(target=ch)
   p3 = Process(target=pk)
   p4 = Process(target=bk)
   p1.start()
   p2.start()
   p3.start()
   p4.start()
   p1.join()
   p2.join()
   p3.join()
   p4.join()