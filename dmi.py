#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script prints the current temperature from Aalborg Airport
'''

import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.dmi.dk/vejr/i-luften/metar-og-taf/'
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

metar_line = soup.find_all("font", text = re.compile('ekyt'))[0].text

temp_line = re.search('\d\d\/', metar_line).group(0)
temp = temp_line.replace('/', '')
print('Temperaturen i Aalborg er ' + temp + '°C')
