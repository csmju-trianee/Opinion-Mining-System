import schedule
import time
import location
import function_l
from importlib import reload
check =0
url =str()
Next_page=str()
def main():
    global check
    global page
    #เช็คสถานที 
    if check==0:
        url = str("/Attraction_Review-g293917-d7133132-Reviews-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html")
        check = check + 1 
    else:
        url = None
        url = page
    #หาลิ้งหน้าสุดท้าย
    Maxpage = int(function_l.value_page(url))
    #page = str(function_l.getlink(url))
    #เริ่มการหาคำ
    function_l.getText(Maxpage)
    
    print(page)
    #update =  Next_page  
    #Next_page = update
    


schedule.every(0).seconds.do(main)

i = 1

while True:
    
    schedule.run_pending()
    print(i)
    time.sleep(1)
    i = i+1
    




