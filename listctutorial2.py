


data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]

### List Comprehension version
col_width = max(len(word) for row in data for word in row) + 2  # padding
print(col_width)
for row in data:
    print ("".join(word.ljust(col_width) for word in row))

print()

### Loop version
col_widths = []
for i in data:
    for j in i:
        col_widths.append(len(j)+2)
col_width = max(col_widths)



for i in data:
    tmp = ''
    for j in i:
        tmp += j.ljust(col_width)
    print(tmp)


