def getDBDetails(port, *arguments):
    print(port)
    for item in arguments:
        print(item)

getDBDetails(5432, "fedser.stack.com", "testdb")
