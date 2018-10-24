import collections

print('Bible analyzer!')
f = open('bible.txt', mode='r', encoding='iso-8859-1')
bibleList = f.read().lower().replace('\n', '').split(' ')
bibleList = [x for x in bibleList if type(x) != int]
bibleData = collections.Counter(bibleList)

rank = 0
for word, count in  bibleData.most_common(101):
    print(str(rank) + ': ' +word.ljust(20, '.') + str(count).rjust(20, '.'))
    rank += 1
    
