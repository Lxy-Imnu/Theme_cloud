import requests
import json
from bs4 import BeautifulSoup
import sys
import importlib
import time
import re

headers ={'User-Agent': 'Mozilla/5.0'}
url = "http://dangjian.people.com.cn/"

def get_page(url,data=None):
    r = requests.get(url,headers=headers)
    soup = BeautifulSoup(r.text,"lxml")
    title_list = soup.find_all("a",target_="_blank")

    for title in title_list:
        data ={
            "标题": title.text.strip(),
            "时间":

        }

