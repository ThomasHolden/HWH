import os
import datetime
import time

if __name__ == '__main__':

    while True:
        now = datetime.datetime.now()
        #speed = os.popen("python /home/thomas/anaconda3/lib/python3.5/site-packages/speedtest.py").read()
        speed = os.popen("python ./.local/lib/python2.7/site-packages/speedtest.py").read()
        lines = speed.split('\n')
        print(speed)

        try:
            testfrom = lines[1].replace('Testing from ','').rstrip('...')
            hostedby = ':'.join(lines[4].replace('Hosted by ','').split(':')[:-1])
            ping = lines[4].split(':')[-1]
            download = lines[6].split(':')[1]
            upload = lines[8].split(':')[1]

            with open('speed.csv','a') as file:
                file.write(','.join([str(now),str(testfrom),str(hostedby),str(ping),str(download),str(upload)]))
                file.write('\n')

        except IndexError:
            print(lines)

        time.sleep(60 * 15)