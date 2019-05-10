import requests
from bs4 import BeautifulSoup
import pymysql.cursors

# Webpage connection
url = "http://www.officialcharts.com/charts/singles-chart/19800203/7501/"
data = requests.get(url);

# Grab title-artist classes and iterate
soup = BeautifulSoup(data.text,'html.parser')
recordList = soup.findAll("div", {"class" : "title-artist",})

# Now iterate over recordList to grab title and artist
for record in recordList:
     title = record.find("div", {"class": "title",}).get_text().strip()
     artist = record.find("div", {"class": "artist"}).get_text().strip()
     print (artist + ': ' + title)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='12345678',
                             db='mydatabase',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
try:
    with connection.cursor() as cursor:

        sql_del = "DELETE FROM artist_song"
        cursor.execute(sql_del)
        connection.commit()
        
        for record in recordList:
            title = record.find("div", {"class": "title",}).get_text().strip()
            artist = record.find("div", {"class": "artist"}).get_text().strip()
            sql = "INSERT INTO `artist_song` (`artist`, `song`) VALUES (%s, %s)"
            cursor.execute(sql, (artist, title))
    connection.commit()
finally:
    connection.close()
