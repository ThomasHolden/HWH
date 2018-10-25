


import pandas as pd
import sqlite3
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from tinydb import TinyDB, Query





def getbrandlinks(brand, soupbrandsource):
    divs = soupbrandsource.find_all('a')
    hrefs = [j.get('href') for j in divs if j is not None and brand.lower() in str(j) and 'index.htm' not in str(j) and '--id' in str(j)]
    return hrefs

def getsourcefromurl(url,driver,closewebdriver=False):
    driver.get(url)
    source = driver.page_source
    if closewebdriver:
        driver.close()
        
    return BeautifulSoup(source, 'lxml')

def parsedata(soupsource):
    elem = soupsource.find('section', {'class': 'specifications p-y-5'}).table

    rows = elem.find_all('tr')
    n = 0

    result = {}

    pricebox = soupsource.find('span', {'class': 'd-block'}).span
    if pricebox.text.lower() != 'price on request':
        print(pricebox.text)
        currency = pricebox.span.text
        price = pricebox.text.replace('{currency}'.format(currency=currency), '').replace(',', '')
        result['Price'] = price
        result['PriceCurrency'] = currency

    for nnr, row in enumerate(rows):
        if len(row.find_all('td')) == 1:
            n = -1
        else:
            tmp = row.find_all('td')
            subtitle = tmp[0].text.strip()
            if subtitle == 'Condition':
                value = tmp[1].a.text.strip()
            else:
                value = tmp[1].text.strip()
        n += 1
        if n > 0:
            result[subtitle] = value

    return result

#### MAIN ####

def mainfunc():
    db = TinyDB('/home/thomas/Python Projects/hwh/watches/db.json')
    User = Query()

    #data = db.search(User.Brand!='asdasdad')
    #data = pd.DataFrame(data)

    print(len(db))

    driver = webdriver.Firefox()
    rooturl = 'https://www.chrono24.com'
    brand = 'sinn'

    cont = True
    startpage = 1
    allbrandpages = []

    while cont:
        print(startpage)
        brandurl = rooturl + "/{brand}/index.htm?man={brand}&pageSize=120&showpage={pagenum}".format(brand=brand,pagenum=startpage)

        print(brandurl)

        brandsource = getsourcefromurl(brandurl,driver,False)
        brandpages = getbrandlinks(brand,brandsource)

        if len(brandpages)>0:
            allbrandpages.extend(brandpages)
            startpage += 1
        else:
            cont = False

        print('brandpage : {}'.format(len(brandpages)))

    print('brandpages : {}'.format(len(allbrandpages)))

    for pagenumber, page in enumerate(allbrandpages):
        if len(db.search(User.page==page)) == 0:
            print(pagenumber,allbrandpages,page)
            full_url = rooturl + page
            watchsource = getsourcefromurl(full_url,driver,False)
            result = parsedata(watchsource)
            result['page'] = page
            db.insert(result)


    driver.close()


if __name__ == '__main__':
    mainfunc()

#out = db.search(User.Brand == 'Rolex')
#pd.DataFrame(out)

