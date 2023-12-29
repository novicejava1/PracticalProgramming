def responseData(request_method, *status, **keywords):
    print(request_method)
    print(status)
    for k in keywords:
        print(keywords[k])

responseData("GET", "200", "OK", cipher="SHA256", protocol="TLS1.2", responsebody="JSON")
