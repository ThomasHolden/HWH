#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import requests
import os
from bs4 import BeautifulSoup

url = sys.argv[1]

page_id = url.split('-')[0].split('/')[-1]
os.makedirs(page_id)

#url = "https://acidcow.com/fun/96869-acid-picdump-91-pics.html"
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')

i = 1
images = []

print('Downloading from ' + url)

for image in soup.find_all("img", alt=re.compile('Acid Picdump')):
    img_src = image.get("src")
    filename = page_id + '-' + img_src.split('/')[-1]
    target_path = '/home/opteron/Downloads/' + page_id + '/' + filename
    print(filename.ljust(20, '.') + 'downloading'.rjust(20, '.'))
    response = requests.get(img_src)
    handle = open(target_path, "wb")
    handle.write(response.content)
    handle.close()
    i += 1

print('Finished: ' + str(i) + ' files downloaded.')
