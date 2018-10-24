


import requests
from bs4 import BeautifulSoup


page = BeautifulSoup(requests.get('https://betbrain.dk/football/denmark/').content,'lxml')
print(page)


