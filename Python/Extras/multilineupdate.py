import time
for i in range(10):
    print('App1 %d\n App2 %d\n App3 %d' % (i, i+1, i+2), end='\r')
    time.sleep(5)
