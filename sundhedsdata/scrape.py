from bs4 import BeautifulSoup
import pandas as pd
import requests

with open('authids.txt') as f:
    testids = f.read().split()

base_url = 'https://autregweb.sst.dk/Authorization.aspx?id='

df = pd.DataFrame()

progress = 0

for _,id in enumerate(testids):
    if round(_/len(testids),2)!=progress:
        print('{:.0%} done'.format(round(_/len(testids),2)))
        progress = round(_/len(testids),2)
    source = requests.get(base_url + id).text
    soup = BeautifulSoup(source,'lxml')
    table = soup.find('div',{'class':'SectionBody'}).table.tbody.find_all('tr')
    rownr = len(df)
    for nnr,i in enumerate(table):
        cols = i.find_all('td')
        if len(cols)>0:
            for nr,c in enumerate(cols):
                if len(c.text.strip())>0:
                    if nr == 0 and nnr > 1:
                        colname = c.text.strip()
                    elif nr == 0 and nnr == 0:
                        colname = c.text.strip()
                    elif nr == 0 and nnr == 1:
                        val = c.text.strip()
                    else:
                        val = c.text.strip()
                    if nr == 1 or nnr == 1:
                        df.loc[rownr,colname] = val

print(df)
df.to_csv('results.csv')

