import time
import sys

print("*" * 60)
print("\tMomentum Metropolitian Services India - Hiring\t")
print("*" * 60)


data = [{'BU': 'Health Solutions', 'Role': 'Cobol Developer'},
        {'BU': 'aYo', 'Role': 'Cyber Security Engineer'},
        {'BU': 'aYo', 'Role': 'Java Developer - USSD'},
        {'BU': 'GuardRisk', 'Role': 'Business Analyst'},
        {'BU': 'MMerge', 'Role': 'RPG Developer - AS400'},
        {'BU': 'Momentum Corporate', 'Role': 'Java Enterprise Developer - J2EE'},
        {'BU': 'Momentum Insure', 'Role': 'Java Angular Developer'},
        {'BU': 'Retail Risk', 'Role': 'Dynamics 365 Developer'},
        {'BU': 'Momentum Investments', 'Role': 'Data Engineer'},
        {'BU': 'Health Solutions', 'Role': 'Technical Test Analyst - Automation'},
        {'BU': 'Group Risk', 'Role': 'Low Code Developer'},
        {'CONTACT': 'Ashchit Chaturvedi', 'Email': 'ashchit.chaturvedi@mmltd.co.za'}

        ]

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

for each in data:

    if 'CONTACT' in each[0]:
        print("\n")
        print("CONTACT  : {}".format(each['CONTACT']))
        print("Email    : ", end='')
        delay_print(each['Email'])        
    else:
        print("\n")
        print("BU       : {}".format(each['BU']))
        print("Role     : ", end='')
        delay_print(each['Role'])

print("\n")