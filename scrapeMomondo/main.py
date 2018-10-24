from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import datetime
import string
import random
import sqlite3

con = sqlite3.connect('flighttickets')

def generateid(length):
    pool = string.ascii_letters + string.digits
    return ''.join(random.choice(pool) for _ in range(length))

#print(airports.loc[idx])
airports = ['LON','MIL','PAR','BER','ROM','ZRH','BUD','BUH','HEL','OSL','STO','EDI','DUB','VIE','TLL','TLS','RIX','AAL']

driver = webdriver.Firefox()

departuredays = pd.date_range(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=180))
departuredays = [j for j in departuredays if j.weekday() == 4]
returndays = [j + datetime.timedelta(days=2) for j in departuredays]

results = pd.DataFrame(columns=['id','Date','Flightservice','DepartureAirport','DepartureTime','Duration','ArrivalAirport','ArrivalTime','Price','PriceUnit','Rating','TimeStamp'])

for date1,date2 in zip(departuredays,returndays):
    for dest in airports:
        id = generateid(64)
        time.sleep(random.randint(1,10))
        for _ in range(2):

            if _ == 0:
                dep_a = 'CPH'
                arr_a = dest
                flytime = date1.strftime('%d-%m-%Y')
            else:
                dep_a = dest
                arr_a = 'CPH'
                flytime = date2.strftime('%d-%m-%Y')

            url = "https://www.momondo.com/flightsearch/?Search=true&TripType=1&SegNo=1&SO0={dep_a}&SD0={arr_a}&SDP0={flytime}&AD=1" \
                      "&TK=ECO&DO=false&NA=false&currency=DKK&cmp2=true".format(dep_a=dep_a,arr_a=arr_a,flytime=flytime)

            print(url)
            driver.get(url)

            progress = ''
            while progress != 'Search complete':
                p_source = driver.page_source
                html = BeautifulSoup(p_source,'lxml')
                progress = BeautifulSoup(p_source,'lxml').find('div',{'id':'searchProgressText'}).text

            print('Ready to find plane ticket prices for the trip {} --> {} on the {}'.format(dep_a,arr_a,flytime))
            timestamp = datetime.datetime.now()
            soup = BeautifulSoup(p_source,'lxml').find('div',{'id':'flight_results'}).div.findChildren()

            for i in soup:
                data = i.find('div',{'class':'result-box-inner'})
                if data is not None:
                    flight = data.find('div',{'class':'names'}).text
                    dep_airport = data.find('div',{'class':'departure'}).find('span',{'class':'iata'}).text
                    dep_time = data.find('div',{'class':'departure'}).find('span',{'class':'time'}).text
                    duration = data.find('div',{'class':'travel-time'}).text
                    dest_airport = data.find('div', {'class': 'destination'}).find('span', {'class': 'iata'}).text
                    dest_time = data.find('div', {'class': 'destination'}).find('span', {'class': 'time'}).text

                    price = i.find('div',{'class':'ticketinfo'}).find('span',{'class':'price'}).find('span',{'class':'value'}).text.replace('.','')
                    rating = i.find('div',{'class':'ticketinfo'}).find('div',{'class':'rating'}).find('span',{'class':'value'}).text
                    priceunit = i.find('div',{'class':'ticketinfo'}).find('span',{'class':'price'}).find('span',{'class':'unit'}).text

                    #print(flight,dep_airport,dep_time,duration,dest_airport,dest_time,price,priceunit)
                    results.loc[len(results)] = [id,flytime,flight,dep_airport,dep_time,duration,dest_airport,dest_time,price,priceunit,rating,timestamp]

            #results.to_csv('results.csv',index=False)
            results.to_sql('FlightTickets',con,if_exists='append',index=False)

driver.close()
time.sleep(10000000)
