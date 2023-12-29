import logging
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start a program')

def factorial(n):
    logging.debug('Start of factorial (%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', totat is ' + str(total))
#    if n != 0:
#        total = n * factorial(n - 1)
#        logging.debug('n is ' + str(n) + ', totat is ' + str(total))
    logging.debug('End of factorial (%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')
