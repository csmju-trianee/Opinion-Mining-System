import link_l
import multiprocessing 
from multiprocessing import Process
if __name__ == '__main__':
   p1 = Process(target=link_l.start_link('ChiangMai',0))
   p2 = Process(target=link_l.start_link('Phuket',1))
   p3 = Process(target=link_l.start_link('Bangkok',2))
   p4 = Process(target=link_l.start_link('Chonburi',3))
   p1.start()
   p2.start()
   p3.start()
   p4.start()
   p1.join()
   p2.join()
   p3.join()
   p4.join()