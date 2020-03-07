import request
from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
html = urlopen("http://www.zhwh365.com/").read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')
all_href = soup.find_all('a')
all_href = [l ['href'] for l in all_href]
print('\n', all_href)
'''
request.GET("http://www.zhwh365.com/")