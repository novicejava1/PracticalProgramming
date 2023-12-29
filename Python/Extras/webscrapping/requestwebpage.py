import requests

try:
    #response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    response = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    response.raise_for_status()
    print(response.status_code)
    print(response.text[:250])
except Exception as err:
    print('There was a problem: %s' % (err))

