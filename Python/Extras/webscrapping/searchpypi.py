import requests, sys, bs4, webbrowser

print('Searching...')
response = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')
linkElems = soup.select('.package-snippet')
#print(linkElems)

numOpen = min(5, len(linkElems))
print(numOpen)
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

