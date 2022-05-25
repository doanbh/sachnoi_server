import json
import math

from bs4 import BeautifulSoup, Tag
from bs4 import NavigableString
from bs4.dammit import EncodingDetector
import re
from urllib.parse import urljoin

import requests

import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)
driver.implicitly_wait(30)


def getDetailRecipe365(link):
    driver.get(link)
    time.sleep(9)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    list_audio = soup.find_all('audio')
    audio = soup.find('div', "jp-jplayer")
    links = [a['src'] for a in soup.find_all('src', href=re.compile('http.*\.mp3'))]
    print(list_audio)
    print(links)
    print(audio)
    # html_ingredients = soup.find("ul", "menu-ingredients")
    # html_step = soup.find("ul", "menu-directions")
    # html_image = soup.find("div", "video-detail_thumb").img
    # content = soup.find("div", "info-intro").text.strip()
    # uid = soup.find("div", "entry-profile").a["href"].replace("/profile/", "").replace(".html", "")
    # if uid == "javascript:void(0)":
    #     uid = 1
    # html_des = soup.find("div", "entry-detail_meta").contents


getDetailRecipe365("https://radiotruyen.info/truyen-kinh-dien/toi-la-thay-tuong-so-audio-quyen-1.html")