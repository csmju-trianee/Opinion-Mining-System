import urllib.request
import urllib.parse
import urllib.response
post_url = 'https://th.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-or10-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html'

headers = {}
headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
post_data = urllib.parse.urlencode({'filterLang' : 'ALL'}).encode('ascii')
#post_data = urllib.parse.urlencode({'preferFriendReviews':'FALSE','t':'','q':'','filterSeasons':'',
            #'filterLang':'ALL','filterSafety':'FALSE','filterSegment':'','trating':'','reqNum':'1','isLastPoll':'false',
            #'paramSeqId':'1','waitTime':'11','changeSet':'REVIEW_LIST','puid':'XNKPMAoQKmEAATCwfbkAAAIh'}).encode('ascii')
post_response = urllib.request.response(post_url)
#urllib.request.urlopen(url=post_url, data=post_data)
print(post_response.read())

