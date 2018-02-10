#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

print('[HWH Navngivningshjælper v. 1.0]')

kandidater = ['Thomas', 'Nikolaj']

def menuvalg():
    valg = input('''-=Menu=-
1: Vis kandidater
2: Tilføj kandidat
3: Indsæt kandidat
4: Slet kandidat
5: Sorter kandidater
6: Find kandidat
7: Vælg kandidat
8: Afslut
Valg: ''')
    if int(valg) == 1:
        print('------------Kandidater------------------')
        for i in range(len(kandidater)):
            print('Kandidat #' + str(i + 1) + ': ' + kandidater[i])
        print('I alt ' + str(len(kandidater)) + ' kandidater')
        print('----------------------------------------')
        menuvalg()
    elif int(valg) == 2:
        print('------------Tilføj kandidat-------------')
        nykandidat = input('Navn: ')
        kandidater.append(nykandidat)
        print('----------------------------------------')
        menuvalg()
    elif int(valg) == 3:
        print('------------Indsæt kandidat-------------')
        nykandidat = input('Navn: ')
        index = int(input('Som nummer: ')) - 1
        kandidater.insert(index, nykandidat)
        print('----------------------------------------')
        menuvalg()
    elif int(valg) == 4:
        print('------------Slet kandidat---------------')
        sletkandidat = input('Navn: ')
        kandidater.remove(sletkandidat)
        print('----------------------------------------')
        menuvalg()
    elif int(valg) == 5:
        print('------------Sorter kandidater-----------')
        kandidater.sort()
        print('Kandidaterne er sorteret ASCIIbetisk')
        print('----------------------------------------')
        menuvalg()
    elif int(valg) == 6:
        print('------------Find kandidat---------------')
        findkandidat = input('Navn: ')
        #print(kandidater.index(findkandidat))
        print('Kandidaten er nummer: ' + str(kandidater.index(findkandidat)+1))
        print('----------------------------------------')
        menuvalg()
    elif int(valg) == 7:
        print('------------Vælg kandidat---------------')
        print('Følgende kandidat er valgt: ' + kandidater[random.randint(0, len(kandidater)-1)])
        print('----------------------------------------')
        menuvalg()
    elif int(valg) == 8:
        print('Tak fordi du valgte HWH software')
    else:
        print('Ugyldigt valg')
        menuvalg()
menuvalg()
