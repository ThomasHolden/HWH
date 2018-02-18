#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Indtast overskrifter til kolonner: (blank = stop)')

titles = []
columnnumb = 1
while columnnumb <= 10:
    title = input('Kolonne #' + str(columnnumb) + ": ")
    if title == "":
        break
    titles.append(title)
    columnnumb += 1

print('Indtast rækker til de ' + str(len(titles)) + ' kolonner: (blank = stop)')

table = []
table.append(titles)

def addrow():
    row = []
    for column in range(len(titles)):
        row.append(input('Indtast værdi for kolonnen ' + titles[column] + ': '))
    table.append(row)

while True:
    addrow()
    if input('Tast "stop" for at stoppe: ') == 'stop':
        break

width = len(titles)*15
print('Tabel:'.center(width, '='))

for row in range(len(table)):
        values = ''
        value = ''
        for index in range(len(table[row])):
            if row == 0:
                value = table[row][index].center(15, ':')
            else:
                value = table[row][index].center(15, ' ')
            values = values + value
        print(values)

print(''.center(width, '='))
