import json
import math

from bs4 import BeautifulSoup, Tag
from bs4 import NavigableString
from bs4.dammit import EncodingDetector
import re

import requests


def getDetailRecipe365(link):
    urlDetail = requests.get(link)
    http_encoding = urlDetail.encoding if 'charset' in urlDetail.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(urlDetail.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(urlDetail.content, 'lxml', from_encoding=encoding)
    list_audio = soup.find_all('audio')
    audio = soup.find_all('div', "chapter-item row")
    links = [a['href'] for a in soup.find_all('a', href=re.compile('http.*\.mp3'))]
    links = [input['value'] for input in soup.find_all('input', value=re.compile('http.*\.mp3'))]
    # print(list_audio)
    # print(audio)
    print(links)
    # html_ingredients = soup.find("ul", "menu-ingredients")
    # html_step = soup.find("ul", "menu-directions")
    # html_image = soup.find("div", "video-detail_thumb").img
    # content = soup.find("div", "info-intro").text.strip()
    # uid = soup.find("div", "entry-profile").a["href"].replace("/profile/", "").replace(".html", "")
    # if uid == "javascript:void(0)":
    #     uid = 1
    # html_des = soup.find("div", "entry-detail_meta").contents


getDetailRecipe365("http://audiolamphong.xyz/story/4312/Hoa-Tinh-Dam-Mau")