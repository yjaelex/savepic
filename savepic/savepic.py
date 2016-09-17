#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import urllib.error
from html.parser import HTMLParser
from bs4 import BeautifulSoup

url = 'http://www.python.org/'
try:
    mainPage = urllib.request.urlopen(url)
    mainHTML = mainPage.read().decode('utf-8')
    print(mainHTML)
except urllib.error.HTTPError as e:
    print("Error Code:", e.code)
except urllib.error.URLError as e:
    print("Error Reason:", e.reason)

soup = BeautifulSoup(mainHTML, 'html.parser')
print(soup.prettify())





