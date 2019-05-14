import requests
import page_number
import function_l
import pymysql
import threading

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def start_link():
    try:   
        sql = "select * from location"
        cursor = connection .cursor()
        cursor.execute(sql)
        link = cursor.fetchall()
        print("Total number of rows in python_developers is - ", cursor.rowcount)

        for i in link:
            urls=str(i["url"])
            print(urls)
            id_review  = urls.split('https://www.tripadvisor.com/')[1].split('Reviews-')
            print(id_review)
            link = urls
            data = requests.get(urls)
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(data.text,'html.parser')
            x = soup.find_all("div",{"class":"more-options"})#comment    
            for i in x:
                print("\n get :",((i.text)),"\n---------------")
                i.text
            try:
                txt = (i.text).split('All languages')
                del txt[0]
            finally:
                pass
            if txt[0].find('Arabic') != -1:
                url = ("www.tripadvisor.com.eg/")
                start = (page_number.page_ar(link))
                thread1 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread1.start()
            
            if txt[0].find('Arabic (Int)') != -1:
                url = ("ar.tripadvisor.com/")
                start = (page_number.page_ae_AE(link))
                thread2 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread2.start()
            
            if txt[0].find('Chinese (Int)') != -1:
                url = ("cn.tripadvisor.com/")
                start = (page_number.page_zh(link))
                thread3 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread3.start()
            
            if txt[0].find('Chinese (Sim.)') != -1:
                url = ("www.tripadvisor.cn/")
                start = (page_number.page_zh_CN(link))
                thread4 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread4.start()
            
            if txt[0].find('Chinese (Trad.)') != -1:
                url = ("www.tripadvisor.com.tw/")
                start = (page_number.page_zh_TW(link))
                thread5 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread5.start()
            
            if txt[0].find('Czech')!= -1:
                url = ("www.tripadvisor.cz/")
                start = (page_number.page_cs(link))
                thread6 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread6.start()

            if txt[0].find('Danish')!= -1:
                url = ("www.tripadvisor.dk/")
                start = (page_number.page_da(link))
                thread7 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread7.start()
        
            if txt[0].find('Dutch')!= -1:
                url = ("www.tripadvisor.nl/")
                start = page_number.page_nl(link) 
                thread8 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread8.start()

            if txt[0].find('English')!= -1:
                url = ("www.tripadvisor.com/")
                start = page_number.page_en(link)
                thread9 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread9.start()

            if txt[0].find('Finnish')!= -1:
                url = ("www.tripadvisor.fi/")
                start = page_number.page_fi(link)
                thread10 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread10.start()
            
            if txt[0].find('French')!= -1:
                url = ("www.tripadvisor.fi/")
                start = page_number.page_fr(link)
                thread11 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread11.start()

            if txt[0].find('French (Bel.)')!= -1:
                url = ("www.tripadvisor.be/")
                start = page_number.page_fr_BE(link)
                thread12 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread12.start()

            if txt[0].find('French (Can.)')!= -1:
                url = ("fr.tripadvisor.ca")
                start = page_number.page_fr_CA(link)
                thread13 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread13.start()

            if txt[0].find('French (Swi.)')!= -1:
                url = ("fr.tripadvisor.ch/")
                start=page_number.page_fr_CH(link)
                thread14 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread14.start()

            if txt[0].find('German')!= -1:
                url = ("www.tripadvisor.de/")
                start = page_number.page_de(link)
                thread15 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread15.start()
            
            if txt[0].find('Greek')!= -1:
                url = ("www.tripadvisor.com.gr/")
                start=page_number.page_el(link)
                thread16 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread16.start()

            if txt[0].find('Hebrew')!= -1:
                url = ("www.tripadvisor.co.il/")
                start=page_number.page_iw(link)
                thread17 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread17.start()
            
            if txt[0].find('Hungarian')!= -1:
                url = ("www.tripadvisor.co.hu/")
                start=page_number.page_hu(link)
                thread18 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread18.start()

            if txt[0].find('Indonesian')!= -1:
                url = ("www.tripadvisor.co.id/")
                start=page_number.page_in(link)
                thread19 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread19.start()

            if txt[0].find('Italian')!= -1:
                url = ("www.tripadvisor.it/")
                start = page_number.page_it(link)
                thread20 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread20.start()

            if txt[0].find('Italian (Swit.)')!= -1:
                url = ("it.tripadvisor.ch/")
                start = page_number.page_it_ch(link)
                thread21 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread21.start()

            if txt[0].find('Japanese')!= -1:
                url = ("www.tripadvisor.jp/")
                start = page_number.page_ja(link)
                thread22 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread22.start()

            if txt[0].find('Korean')!= -1:
                url = ("www.tripadvisor.co.kr/")
                start=page_number.page_ko(link)
                thread23 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread23.start()

            if txt[0].find('Norwegian')!= -1:
                url = ("no.tripadvisor.com/")
                start=page_number.page_no(link)
                thread24 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread24.start()

            if txt[0].find('Polish')!= -1:
                url = ("pl.tripadvisor.com/")
                start=page_number.page_pl(link)
                thread25 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread25.start()

            if txt[0].find('Portuguese')!= -1:
                url = ("www.tripadvisor.pt/")
                start=page_number.page_pt(link)
                thread26 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread26.start()

            if txt[0].find('Russian')!= -1:
                url = ("www.tripadvisor.ru/")
                start=page_number.page_ru(link)
                thread27 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread27.start()

            if txt[0].find('Serbian')!= -1:
                url = ("www.tripadvisor.rs/")
                start=page_number.page_sr(link)
                thread28 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread28.start()

            if txt[0].find('Slovak')!= -1:
                url = ("www.tripadvisor.sk/")
                start=page_number.page_sk(link)
                thread29 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread29.start()

            if txt[0].find('Spanish')!= -1:
                url = ("www.tripadvisor.es/")
                start=page_number.page_es(link)
                thread30 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread30.start()

            if txt[0].find('Swedish')!= -1:
                url = ("www.tripadvisor.se/")
                start=page_number.page_sv(link)
                thread31 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread31.start()

            if txt[0].find('Thai')!= -1:
                url = ("th.tripadvisor.com/")
                start=page_number.page_th(link)
                thread32 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread32.start()

            if txt[0].find('Turkish')!= -1:
                url = ("www.tripadvisor.com.tr/")
                start=page_number.page_tr(link)
                thread34 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread34.start()

            if txt[0].find('Vietnamese')!= -1:
                url = ("www.tripadvisor.com.vn/")
                start=page_number.page_vi(link)
                thread35 = threading.Thread(target = function_l.getText(url,id_review,start))
                thread35.start()
            
        
        cursor.close()
    finally:
        #closing database connection.
        connection.close()
        print("MySQL connection is closed")
