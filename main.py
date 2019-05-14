import schedule
import time
import location
import function_l
from importlib import reload
def main():
#สถานที่ท่องเที่ยว

#โรงแรม

#ร้านอาหาร
    


schedule.every(0).seconds.do(main)

i = 1

while True:
    
    schedule.run_pending()
    print(i)
    time.sleep(1)
    i = i+1
    




