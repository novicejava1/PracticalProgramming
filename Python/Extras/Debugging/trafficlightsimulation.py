#market_2nd = {'ns': 'green', 'ew': 'red'}
market_2nd = {'ns': 'green', 'ew': 'yellow'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    assert 'red' in stoplight.values(), 'Neither light in red' + str(stoplight)
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

switchLights(market_2nd)
