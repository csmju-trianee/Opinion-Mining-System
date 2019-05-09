import urllib.request

# https://docs.python.org/3/library/urllib.request.html#examples
# "Here is an example of doing a PUT request using Request:"
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
req = urllib.request.Request(url='https://www.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html', headers=header, method='POST')
res = urllib.request.urlopen(req, timeout=5)

print(res.status)
print(res.reason)