import requests
import function_l
province = ['https://www.tripadvisor.com/Attractions-g1308496-Activities-Chiang_Mai_Province.html',
            'https://www.tripadvisor.com/Attractions-g293920-Activities-Phuket.html',
            'https://www.tripadvisor.com/Attractions-g293916-Activities-Bangkok.html']

def cm():
    data = requests.get(province[0])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("a",{"rel":"noopener noreferrer"},"href=")
    category=[]
    for i in x:
        if i.get('href').find('Activities') != -1: 
            if i.get('href').find('Chiang_Mai_Province') != -1:
                #print(i.get('href'))
                category.append(i.get('href'))
    function_l.list_category(category)



def pk():
    data = requests.get(province[1])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("a",{"rel":"noopener noreferrer"},"href=")
    category=[]
    for i in x:
        if i.get('href').find('Activities') != -1: 
            category.append(i.get('href'))
            print(category)
            

def pk():
    data = requests.get(province[2])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("a",{"rel":"noopener noreferrer"},"href=")
    category=[]
    for i in x:
        if i.get('href').find('Activities') != -1: 
            category.append(i.get('href'))
            print(category)



        
