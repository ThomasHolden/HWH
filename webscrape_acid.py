#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 This script downloads pictures from "Picdumps" at acidcow.com.
 Usage: ./webscrape.py [start_page] [end_page]
 Pictures will be saved in save_path
 I recommend adding this script to cron
'''


import re
import requests
import sys
from bs4 import BeautifulSoup


# PicDump-scraper

def pd_scraper(pd_link):
    save_path = '/home/opteron/K-Drive/code/Acidcow/Images/'    #Change if needed
    page_id = pd_link.split('-')[0].split('/')[-1]
    page = requests.get(pd_link)
    pd_soup = BeautifulSoup(page.content, 'html.parser')

    i = 1

    print('Downloading from: ' + url)

    for image in pd_soup.find_all("img", alt=re.compile('Acid Picdump')):
        img_src = image.get("src")
        filename = page_id + '-' + img_src.split('/')[-1]
        target_path = save_path + filename
        print(filename.ljust(20, '.') + 'downloading'.rjust(20, '.'))
        pd_response = requests.get(img_src)
        handle = open(target_path, "wb")
        handle.write(pd_response.content)
        handle.close()
        i += 1

    print('Finished: ' + str(i) + ' files downloaded.')





# Scraping through the pages

start_page = sys.argv[1]
end_page = sys.argv[2]

baseurl = 'https://acidcow.com/page/'
urls = []

for page in range(int(start_page), int(end_page)+1):
    urls.append(baseurl + str(page) + '/')

for url in urls:
    print('Page: ' + url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pd_link = soup.find_all('a', string=re.compile('Acid Picdump'))[0].get('href')
    pd_scraper(pd_link)


response.close()

