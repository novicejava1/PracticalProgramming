import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')

print(type(elems))
print(len(elems))
print(str(elems[0].attrs))
print(str(elems[0].getText()))

