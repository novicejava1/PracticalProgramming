import requests, bs4

try:
    response = requests.get('https://nostarch.com')
    response.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(response.text, 'html.parser')
    print(type(noStarchSoup))
except Exception as err:
    print(err)
