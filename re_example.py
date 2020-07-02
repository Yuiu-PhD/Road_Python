import re

hand1 = open('/Users/yu/Documents/Code/Python/Road_Python/mbox-short.txt')
# Search for lines that start with 'From'
print("Search for lines that start with 'From'")
for line1 in hand1:
    line1 = line1.rstrip()
    if re.search('^From:', line1):
        print(line1)

hand2 = open('/Users/yu/Documents/Code/Python/Road_Python/mbox-short.txt')
# Search for lines that start with 'F', followed by 2 characters, followed by 'm:'
print("Search for lines that start with 'F', followed by 'm:'")
for line2 in hand2:
    line2 = line2.rstrip()
    if re.search('^F..m:', line2):
        print(line2)

hand3 = open('/Users/yu/Documents/Code/Python/Road_Python/mbox-short.txt')
# Search for lines that start with From and have an at sign
print("Search for lines that start with From and have an at sign")
for line3 in hand3:
    line3 = line3.rstrip()
    if re.search('^From:.+@', line3):
        print(line3)

hand4 = open('/Users/yu/Documents/Code/Python/Road_Python/mbox-short.txt')
# Search for lines that have an at sign between characters
print("Search for lines that have an at sign between characters")
for line4 in hand4:
    line4 = line4.rstrip()
    x4 = re.findall('\S+@\S+', line4)
    if len(x4) > 0:
        print(x4)

hand5 = open('/Users/yu/Documents/Code/Python/Road_Python/mbox-short.txt')
# Search for lines that have an at sign between characters
# The characters must be a letter or number
print("Search for lines that have an at sign between characters and the characters must be a letter or number")
for line5 in hand5:
    line5 = line5.rstrip()
    x5 = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line5)
    if len(x5) > 0:
        print(x5)

hand6 = open('/Users/yu/Documents/Code/Python/Road_Python/mbox-short.txt')
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
print("Search for lines that start with 'X' followed by any non whitespace characters and ':' followed by a space and any number")
for line6 in hand6:
    line6 = line6.rstrip()
    if re.search('^X\S*: [0-9.]+', line6):
        print(line6)
    x6 = re.findall('^X\S*: ([0-9.]+)', line6)
    if len(x6) > 0:
        print(x6)
