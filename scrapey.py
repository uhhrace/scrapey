# Compare mean price 3be2br homes in SD / LA 
# 40 homes from each, variety of areas, 10 counties, 4 from each
https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
https://medium.com/bugbountywriteup/bypassing-captcha-like-a-boss-d0edcc3a1c1
https://www.raymond.cc/blog/bypass-captcha-firefox-auto-solving-captcha-monster/
https://www.quora.com/Is-there-any-way-to-skip-CAPTCHA
https://github.com/mikeyy/nonocaptcha

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import asyncio
from nonocaptcha.solver import Solver

url = "https://www.zillow.com/el-cajon-ca-92020/3-3_beds/2.0-_baths/?searchQueryState={%22pagination%22:{},%22usersSearchTerm%22:%2292020%22,%22mapBounds%22:{%22west%22:-117.06762690551761,%22east%22:-116.86678309448246,%22south%22:32.73376868883979,%22north%22:32.8541170587933},%22regionSelection%22:[{%22regionId%22:96589,%22regionType%22:7}],%22isMapVisible%22:false,%22mapZoom%22:13,%22filterState%22:{%22beds%22:{%22min%22:3,%22max%22:3},%22baths%22:{%22min%22:2}},%22isListVisible%22:true}"

response = requests.get(url)

soup = BeautifulSoup(response.text, “html.parser”)

