import traceback

def spam():
    bacon()

def bacon():
    try:
        raise Exception('This is the error message')
    except:
        errorFile = open('errorInfo.txt', 'w')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print("Traceback information written to file errorInfo.txt")

spam()
