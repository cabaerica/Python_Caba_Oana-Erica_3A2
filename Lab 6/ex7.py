import re

def validateCNP():
    cnp = input('Enter CNP: ')
    if re.match(r'^^[1-9]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])(0[1-9]|[1-4]\d|5[0-2]|99)(00[1-9]|0[1-9]\d|[1-9]\d\d)\d$', cnp):
        print('Valid CNP')
    else:
        print('Invalid CNP')


def main():
    validateCNP()

main()