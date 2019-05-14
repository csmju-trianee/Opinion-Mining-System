import requests
def page_ar(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"ar"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break
       
def page_ae_AE(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"ae"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_zh(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"zh"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_zh_CN(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"zhCN"},"span")
    for i in x:
       try:
              txt = str(i.text.split('Chinese (Sim.) (')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break
    
def page_zh_TW(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"zhTW"},"span")
    for i in x:
       try:
              txt = str(i.text.split('Chinese (Trad.) (')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break
    
def page_cs(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"cs"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_da(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"da"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_nl(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"nl"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_en(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"en"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break
    
def page_fi(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"fi"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_fr(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"fr"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break


def page_fr_BE(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"frBE"},"span")
    for i in x:
       try:
              txt = str(i.text.split('French (Bel.) (')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_fr_CA(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"frCA"},"span")
    for i in x:
       try:
              txt = str(i.text.split('French (Can.) (')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_fr_CH(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"frCH"},"span")
    for i in x:
       try:
              txt = str(i.text.split('French (Swit.) (')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_de(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"de"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_el(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"el"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_iw(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"iw"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_hu(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"hu"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_in(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"in"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_it(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"it"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_it_ch(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"itCH"},"span")
    for i in x:
       try:
              txt = str(i.text.split('Italian (Switzerland)(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_ja(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"ja"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_ko(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"ko"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_no(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"no"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_pl(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"pl"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_pt(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"pt"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_ru(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"ru"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_sr(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"sr"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break
    
def page_sk(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"sk"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_es(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"es"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_sv(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"sv"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_th(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"th"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_tr(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"tr"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break

def page_vi(link):
    url = link
    data = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data.text,'html.parser')
    x = soup.find_all("div",{"data-value":"vi"},"span")
    for i in x:
       try:
              txt = str(i.text.split('(')[1].split(')')[0])
              newstr = txt.replace(",", "")
       except:
              pass
       finally:
              return(int(newstr))
              break
